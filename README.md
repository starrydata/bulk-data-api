# Project Description

This project fetches JSON data for various combinations of physical quantities and performs unit conversions.

## About v1

v1 is a version of the JSON output where the units have been converted to the expected ones.
The output directory is set to `dist/v1`.

## API Specification

- OpenAPI specification: [openapi.yaml](https://starrydata.github.io/cleansing-dataset/v1/openapi.yaml)
- Example graph data: [Temperature-ZT.json](https://starrydata.github.io/cleansing-dataset/v1/Temperature-ZT.json)
- Graph list: [graph_list.json](https://starrydata.github.io/cleansing-dataset/v1/graph_list.json)

### Endpoints

- `/v1/{prop_x}-{prop_y}.json` : Graph data for the specified property combination (JSON)
- `/v1/graph_list.json` : List of all graphs and their counts (JSON)

For detailed specifications, see [openapi.yaml](https://starrydata.github.io/cleansing-dataset/v1/openapi.yaml).
