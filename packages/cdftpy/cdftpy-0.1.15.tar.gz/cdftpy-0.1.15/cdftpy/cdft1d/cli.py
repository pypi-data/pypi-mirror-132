#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Command line interface to 1D CDFT calculations
"""

import datetime
import json
import pathlib
import sys

import click
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.shortcuts import confirm
from prompt_toolkit.validation import Validator

from cdftpy.cdft1d.config import DATA_DIR
from cdftpy import __version__
from cdftpy.cdft1d.workflow import cdft1d_single_point, cdft1d_multi_solute

HEADER = """
==================================
1D-CDFT PROGRAM

Marat Valiev and Gennady Chuev
==================================
"""


def cdft1d_generate_input():
    def is_float(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def is_empty(line):
        return line.strip() != ""

    def file_exist(filename):
        filename = filename + ".dat"
        filepath = pathlib.Path.cwd() / filename
        one_word = filename.strip().find(" ") == -1
        not_blank = filename.strip() != ""
        return one_word and not_blank

    validator = Validator.from_callable(
        is_float, error_message="This input is invalid number", move_cursor_to_end=True
    )
    validator_file = Validator.from_callable(
        file_exist, error_message="Bad filename", move_cursor_to_end=True
    )

    validator_empty = Validator.from_callable(
        is_empty, error_message="input cannot be blank", move_cursor_to_end=True
    )

    history = InMemoryHistory()
    history.append_string("rism")
    history.append_string("rsdft")
    history.append_string("s2_rsdft")
    history.append_string("s2_rism")

    with open(DATA_DIR / "ion_data.json") as fp:
        ion_data = json.load(fp)

    while True:
        try:

            prompt(
                "Simulation type: ",
                accept_default=True,
                default=" Single ion solvation",
            )

            solvent = prompt("Solvent model: ", default="s2")
            print("Provide ion parameters")
            name = prompt("  name: ", validator=validator_empty)

            name = name.lower()
            if name in ion_data:
                default_charge = str(ion_data[name]["charge"])
                default_eps = str(ion_data[name]["eps"])
                default_sigma = str(ion_data[name]["sigma"])
            else:
                default_charge = ""
                default_eps = ""
                default_sigma = ""

            charge = prompt("  charge: ", validator=validator, default=default_charge)
            eps = prompt(
                "  \u03B5 (kj/mol): ", validator=validator, default=default_eps
            )
            sigma = prompt("  \u03C3 (Å): ", validator=validator, default=default_sigma)

            rdf_analysis = prompt("RDF Analysis y/n?:") == "y"
            rdf_output = prompt("RDF Output y/n?: ") == "y"

            while 1:
                input_file = prompt(
                    "Choose name for the input file: ",
                    default=f"{name}.dat",
                    validator=validator_file,
                )
                filepath = pathlib.Path.cwd() / input_file
                if filepath.exists():
                    answer = confirm(
                        f"File {input_file} exists. Overwrite? ", suffix="y/N: "
                    )
                    if answer:
                        break
                    continue
                break

            now = datetime.datetime.now()
            with open(input_file, "w") as fp:
                fp.write("# Input file for single ion solvation calculation\n")
                fp.write(f"# generated on {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
                fp.write("<solute>\n")
                fp.write(f"#name  sigma  eps charge \n")
                fp.write(f" {name}  {sigma} {eps} {charge} \n")
                fp.write("<simulation>\n")
                fp.write(f"solvent {solvent}\n")
                if rdf_analysis:
                    fp.write(f"<analysis>\n")
                    fp.write(f"rdf_peaks\n")
                if rdf_output:
                    fp.write(f"<output>\n")
                    fp.write(f"rdf\n")

            print(f"Generated input file {input_file}")

        except EOFError:
            quit(1)
        except KeyboardInterrupt:
            quit(0)
        else:
            break

    return input_file


# noinspection PyTypeChecker
@click.command()
@click.argument("input_file", default="")
@click.option("-m","--method", default='rsdft',
              type=click.Choice(['rism','rsdft'], case_sensitive=False),
              show_default=False,
              help="Calculation method (default:rsdft)")
@click.option("-s","--solvent", "solvent_model",default='s2', type=str,
              metavar="<solvent model>",
              show_default=True,
              help="solvent model")
@click.option("-d","--dashboard",is_flag=False, flag_value="browser", default=None,
              metavar="[filename]",
              type=click.Path(),
              help="Generate dashboard for analysis. The dashboard will be saved as html file "
                   "under the name provided by optional argument. In the absence of the latter "
                   "dashboard will be open in browser")
@click.option("-r","--range", "scan", default=None, type=(str, str),
              metavar='[charge|sigma|eps] <values>',
              help="""Run calculation over the range of solute "charge","sigma","eps" values. Values could specified as
                    array (e.g. [0,0.5,...] or in triplets notation [start]:stop:nsteps
                   """)
@click.option("--version", is_flag=True, help="display version")
def cdft_cli(input_file, method, solvent_model, version, scan, dashboard):
    """
    Perform CFT calculation

    Args:
        input_file

    """


    if version:
        print(__version__)
        sys.exit(0)

    if input_file == "":
        print('Input file is required to run the calculation\n')
        value = click.prompt('Should I generate one? ', default="N")
        if value == 'y':
            input_file = cdft1d_generate_input()
        else:
            sys.exit(1)

    print(F"{scan=}")
    if scan is not None:
        var = scan[0]
        seq = scan[1]
        try:
            start, stop, nsteps = parse_triplet_range(seq)
        except ValueError:
            print(F"Cannot parse scan option {seq}")
            sys.exit(1)
        try:
            values = parse_float_list(seq)
        except ValueError:
            print(F"Cannot parse scan option {seq}")
            sys.exit(1)
        print(F"{seq=}")
        print(F"{values=}")
        cdft1d_multi_solute(input_file, method, solvent_model, var,
                            values=values,
                            stop=stop,
                            nsteps=nsteps,
                            start=start,
                            dashboard = dashboard
                            )
    else:
        cdft1d_single_point(input_file, method, solvent_model, dashboard = dashboard)



def parse_triplet_range(buffer):
    triplet = (None,None,None)
    if ":" in buffer:
        print ("it is triplet")
        buffer = buffer.split(':')
        buffer = [float(x) if x!='' else None for x in buffer ]
        triplet = (buffer[0],buffer[1], int(buffer[2]))
    return triplet

def parse_float_list(buffer):
    float_list = None
    if "," in buffer:
        print("it is list")
        buffer = buffer.split(',')
        float_list = [float(x) if x!='' else None for x in buffer ]
    return float_list

# noinspection PyTypeChecker
@click.command()
@click.argument("input_file", default="")
@click.option("-m","--method", default=None,
              type=click.Choice(['rism','rsdft'], case_sensitive=False))
@click.option("--version", is_flag=True, help="display version")
@click.option("--serve", is_flag=True, help="open browser for calculation analysis")
@click.option("-o", "--output", default=None, type=str,
              help="save output into file, format is inferred from extension, "
                   "only html files are currently supported")
@click.option("--sweep", default=None,
              type=click.Choice(['charge','eps','sigma'], case_sensitive=False))
@click.option("--values", default=None, type=str)
@click.option("--range", "arange",default=None, type=str)
def cdft_cli_save(input_file, method, version, serve, output, sweep, values, arange):
    """
    Perform 1D RISM calculation

    Args:
        input_file

    """

    if version:
        print(__version__)
        sys.exit(0)

    print(values,arange, sweep)
    # if input_file == "":
    #     input_file = cdft1d_generate_input()

    if sweep is not None:
        if values is None and arange is None:
            print("sweep option requires either values or range")
            sys.exit(1)

        start, stop, nsteps = None, None, 11

        if values is not None:
            values = values.split(',')
            values = [float(v) for v in values]
            print(F"{values=}")
        else:
            arange = arange.split(',')
            arange = [float(v) for v in arange]
            if len(arange) == 3:
                start, stop, nsteps = arange
            elif len(arange) == 2:
                stop, nsteps = arange
                print(stop,nsteps)
            elif len(arange) == 1:
                stop = arange
            else:
                print("incorrect format for range")
        if values is not None and arange is not None:
            print("ignoring range option since values were provided")

        nsteps = int(nsteps)
        print(start, stop, nsteps)

        cdft1d_multi_solute(input_file, method, sweep,
                            values=values,
                            stop=stop,
                            nsteps=nsteps,
                            start=start
                            )

    # cdft1d_single_point(input_file, "rsdft", html_serve=serve, html_file = output)

if __name__ == '__main__':
    values = parse_triplet_range('-1:0:10')
    print(values)