#!/usr/bin/env sh

CARLA_VERSION="${CARLA_VERSION:-"$(git rev-parse --abbrev-ref HEAD)"}"
OUTPUT_DIR="${OUTPUT_DIR:-./dist}"
LOG_LEVEL="${LOG_LEVEL:-error}"
PYTHON_BIN="${PYTHON_BIN:-python}"

repo_dir="carla_repo"
temp_doc_dir="$(mktemp -d)"
temp_dist_dir="$(mktemp -d)"

info() {
    echo "- info: $@"
}

error() {
    echo "- error: $@"
}

setup() {
    if [ -d "$OUTPUT_DIR" ]; then
        info 'dist dir exist, abort'
        clear_temp
        exit 1
    fi
}

checkout() {
    info "cloning carla ($CARLA_VERSION) from remote ..."
    if [ -d "$repo_dir" ]; then
        git -C "$repo_dir" checkout -q "$CARLA_VERSION"
    else
        git clone \
            -b "$CARLA_VERSION" \
            --depth 1 \
            https://github.com/carla-simulator/carla.git "$repo_dir"
    fi
    local status=$?
    if [ $status -eq 0 ]; then
        info 'checkout done, copying docs to doc-dir ...'
    else
        error 'failed to checkout carla, abort'
        clear_temp
        exit 1
    fi
    cp "$repo_dir"/PythonAPI/docs/*.yml "$temp_doc_dir" 
}

generate_stub_files() {
    info 'generating stub files from docs ...'
    "$PYTHON_BIN" -m carla_doc \
                -l "$LOG_LEVEL" \
                -i "$temp_doc_dir" \
                --patches-root ./doc_patches \
                --extra-root ./extra_docs \
                -o "$temp_dist_dir"
    local status=$?
    if [ $status -eq 0 ]; then
        info 'stub files generated'
    else
        error 'failed to generate stub files, pls check the log, abort'
        clear_temp
        exit 1
    fi
}

format_stub_files() {
    info 'formatting ...'
    "$PYTHON_BIN" -m ruff format -s "$temp_dist_dir"
    local status=$?
    if [ $status -eq 0 ]; then
        info 'formatting done'
    else
        error 'failed to format, must be corruptions in stub files, pls check the log, abort'
        clear_temp
        exit 1
    fi
}

clear_temp() {
    info 'cleaning temp dirs ...'
    rm -rf "$temp_doc_dir" "$temp_dist_dir"
}

setup

checkout

generate_stub_files

format_stub_files

mv "$temp_dist_dir" "$OUTPUT_DIR"

clear_temp
