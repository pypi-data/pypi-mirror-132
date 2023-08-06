"""Unity type tree generator CLI."""
import os
import logging
from logging import LogRecord
from logging import StreamHandler
from argparse import ArgumentParser

from typetree_unity import TypeTreeGenerator
from typetree_unity import __version__

class _NoStackTraceStreamHandler(StreamHandler):
    """Does not emit caught exception stack trace to stream."""

    __doc__ += StreamHandler.__doc__

    def emit(self, record):  # noqa: D102
        try:
            if record.exc_info:
                record = LogRecord(
                    record.name, record.levelname, record.pathname, record.lineno,
                    record.msg, record.args, None, record.funcName, record.stack_info
                )
            super().emit(record)
        except Exception:  # pylint: disable=broad-except
            self.handleError(record)

def main():
    """Entry point when run from a terminal."""
    logging.info("Running in CLI mode")
    console = _create_console_handler()
    args = _get_args()

    if args.enable_debug_output:
        console.setLevel(logging.DEBUG)

    generator = TypeTreeGenerator(args.assembly_folder, args.unity_version)
    trees = {}
    for class_name in args.class_names:
        trees.update(generator.generate_tree(args.assembly_file, class_name))

    if trees:
        if args.names_only:
            trees = list(trees.keys())
            trees.sort()

        generator.export_tree(trees, args.output_file)
    else:
        logging.info("Type tree did not generate")

def _get_args():
    default_output_folder = os.path.join(
        os.path.dirname(__file__),
        "output"
    )
    default_assembly_filename = "Assembly-CSharp.dll"
    default_typetree_name = "typetree"
    default_classname_name = "classnames"

    parser = ArgumentParser(
        description="Generates type trees from Unity assemblies and outputs in JSON format."
    )
    parser.add_argument(
        "assembly_folder",
        metavar="input_folder",
        help="folder containing assemblies"
    )
    parser.add_argument(
        "unity_version",
        help="Unity build version"
    )
    parser.add_argument(
        "-a",
        "--assembly",
        dest="assembly_file",
        default=default_assembly_filename,
        metavar="",
        help=f"assembly file to load (default: {default_assembly_filename})"
    )
    parser.add_argument(
        "-c",
        "--classes",
        dest="class_names",
        default=[""],
        nargs="*",
        metavar="",
        help="classes to dump for the type tree (all if unspecified). "
            + "Automatically dumps class dependencies."
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output_file",
        metavar="",
        help=f"type tree output file (default: {default_output_folder}{os.path.sep}"
            + f"{default_typetree_name}.json)."
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=__version__,
        help="version of this package"
    )
    parser.add_argument(
        "-n",
        "--namesonly",
        dest="names_only",
        action="store_true",
        help=f"only output class names (will output as {default_classname_name}"
            + ".json if output is not specified)"
    )
    parser.add_argument(
        "-d",
        "--debug",
        dest="enable_debug_output",
        action="store_true",
        help="enable debug output"
    )

    args = parser.parse_args()

    if args.output_file:
        output_dir, file_name = os.path.split(args.output_file)
        if not output_dir:
            args.output_file = os.path.join(default_output_folder, file_name)
    else:
        args.output_file = os.path.join(
            default_output_folder,
            (default_classname_name if args.names_only else default_typetree_name) + ".json"
        )
    return args

def _create_console_handler():
    console = _NoStackTraceStreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter('%(message)s'))
    logging.getLogger().addHandler(console)
    return console

main()
