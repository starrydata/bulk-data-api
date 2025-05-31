# Starrydata Bulk Data API

This project provides static JSON data for all combinations of physical quantities in Starrydata, including unit conversions.

## About v1

v1 is a version of the JSON output where the units have been converted to the expected ones.
The output directory is set to `dist/v1`.

## API Specification

- OpenAPI specification: [openapi.yaml](https://starrydata.github.io/bulk-data-api/v1/openapi.yaml)
- Example graph data: [Temperature-ZT.json](https://starrydata.github.io/bulk-data-api/v1/Temperature-ZT.json)
- Graph list: [graph_list.json](https://starrydata.github.io/bulk-data-api/v1/graph_list.json)

### Endpoints

- `/v1/{prop_x}-{prop_y}.json` : Graph data for the specified property combination (JSON)
- `/v1/graph_list.json` : List of all graphs and their counts (JSON)

For detailed specifications, see [openapi.yaml](https://starrydata.github.io/bulk-data-api/v1/openapi.yaml).
