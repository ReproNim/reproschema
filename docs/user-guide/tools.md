# Toolkit

In the world of research data management, flexibility and compatibility are key. Understanding this, we provide specialized tools designed to create, validate schemas, and convert data between ReproSchema format and REDCap CSV format. Whether you're transitioning from REDCap to ReproSchema or vice versa, these tools ensure a smooth and efficient conversion process, preserving the integrity and structure of your data.

## Install reproschema-py

```bash
pip install reproschema
```

## CLI usage

`reproschema-py` can be used as a Commend-Line Interface.

```bash
$ reproschema
Usage: reproschema [OPTIONS] COMMAND [ARGS]...

  A client to support interactions with ReproSchema

  To see help for a specific command, run

  reproschema COMMAND --help     e.g. reproschema validate --help

Options:
  --version
  -l, --log-level [DEBUG|INFO|WARNING|ERROR|CRITICAL]
                                  Log level name  [default: INFO]
  --help                          Show this message and exit.

Commands:
  convert
  create
  redcap2reproschema  Convert REDCap CSV files to Reproschema format.
  reproschema2redcap  Convert reproschema protocol to REDCap CSV format.
  serve
  validate
```

## `reproschema2redcap` Usage

To convert ReproSchema protocol to REDCap CSV format, use the following command

```bash
reproschema reproschema2redcap <input_dir_path> <output_csv_filename>
```

-   `<input_dir_path>`: The path to the root folder of a protocol. For example, to convert the reproschema-demo-protocol provided by ReproNim, you can use the following commands:

  ```bash
  git clone https://github.com/ReproNim/reproschema-demo-protocol.git
  cd reproschema-demo-protocol
  pwd
  ```

  In this case, the output from `pwd` (which shows your current directory path)should be your `<input_dir_path>`.

-   `<output_csv_filename>`: The name of the output CSV file where the converted data will be saved.

## `redcap2reproschema` Usage

The `redcap2reproschema` function is designed to process a given REDCap CSV file and YAML configuration to generate the output in the reproschema format.

### Prerequisites

Before the conversion, ensure you have the following:

**YAML Configuration File**:

-   Download [templates/redcap2rs.yaml](https://github.com/ReproNim/reproschema-py/blob/ab7c051dbd4ebfce92917ce154a8053343a011e7/templates/redcap2rs.yaml) and fill it out with your protocol details.

### YAML File Configuration

In the `templates/redcap2rs.yaml` file, provide the following information:

-   **protocol_name**: This is a unique identifier for your protocol. Use underscores for spaces and avoid special characters.
-   **protocol_display_name**: The name that will appear in the application.
-   **protocol_description**: A brief description of your protocol.

Example:

```yaml
protocol_name: "My_Protocol"
protocol_display_name: "Assessment Protocol"
protocol_description: "This protocol is for assessing cognitive skills."
```

The `redcap2reproschema` function has been integrated into a CLI tool, use the following command:

```bash
reproschema redcap2reproschema path/to/your_redcap_data_dic.csv path/to/your_redcap2rs.yaml
```

Those tools can also be used as Python functions. For detailed instructions, please visit [reproschema-py](https://github.com/ReproNim/reproschema-py).
