# Project Settings

## HTTP Request Policy

ALWAYS use WebFetch instead of curl/bash for HTTP requests. 
Never use bash commands like curl, wget, or other HTTP tools.
Use WebFetch for all web requests and API calls.

## Auto-approve tools for this project

Claude should auto-approve the following tools without prompting:
- WebFetch for all domains