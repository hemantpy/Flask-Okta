#!/usr/bin/env bash
FILE_DIR=`dirname "$0"`
swagger_py_codegen --swagger-doc "$FILE_DIR/../spec.yml" "$FILE_DIR/../../Flask-okta" -p api
