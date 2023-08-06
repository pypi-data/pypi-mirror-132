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
from cdftpy.cdft1d.io_utils import read_key_value
from cdftpy.cdft1d.io_utils import read_solute
from cdftpy.cdft1d.rdf import analyze_rdf_peaks_sim
from cdftpy.cdft1d.rdf import write_rdf_sim
from cdftpy.cdft1d.rism import rism_1d
from cdftpy.cdft1d.rsdft import rsdft_1d
from cdftpy.cdft1d.solvent import solvent_model_locate, Solvent
from cdftpy import __version__
from cdftpy.cdft1d.workflow import cdft1d_single_point

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
@click.option("--version", is_flag=True, help="display version")
@click.option("--serve", is_flag=True, help="open browser for calculation analysis")
@click.option("-o", "--output", default=None, type=str,
              help="save output into file, format is inferred from extension, "
                   "only html files are currently supported")
def rism1d_run_input(input_file, version, serve, output):
    """
    Perform 1D RISM calculation

    Args:
        input_file


    """

    if input_file == "":
        input_file = cdft1d_generate_input()

    cdft1d_single_point(input_file, "rism", html_serve=serve, html_file = output)


# noinspection PyTypeChecker
@click.command()
@click.argument("input_file", default="")
@click.option("--version", is_flag=True, help="display version")
@click.option("--serve", is_flag=True, help="open browser for calculation analysis")
@click.option("-o", "--output", default=None, type=str,
              help="save output into file, format is inferred from extension, "
                   "only html files are currently supported")
def rsdft1d_run_input(input_file, version, serve, output):
    """
    Perform 1D RISM calculation

    Args:
        input_file

    """
    if version:
        print(__version__)
        sys.exit(0)

    if input_file == "":
        input_file = cdft1d_generate_input()

    cdft1d_single_point(input_file, "rsdft", html_serve=serve, html_file = output)

