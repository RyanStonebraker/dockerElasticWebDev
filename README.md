# Overview
Example docker configuration with:
- Elastic Search
- Kibana
- Custom elasticsearch populate script
- Flask
- Special python requirements

## Customization
The populate script contains a simple while loop that checks for elastic search to start before executing and adding data.
After the populate script executes, the simple flask server starts at http://localhost.
