# dockerElasticWebDev
Example configuration of docker with elastic search, kibana, a custom populate script, and Flask.

## Customization
The populate script contains a simple while loop that checks for elastic search to start before executing and adding data.
After the populate script executes, the simple flask server starts at http://localhost
