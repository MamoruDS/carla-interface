#!/usr/bin/env sh

CARLA_VERSION="${1:-$CARLA_VERSION}"
CARLA_VERSION="${CARLA_VERSION:-"$(git rev-parse --abbrev-ref HEAD)"}"

REPO_DIR=${REPO_DIR:-./temp/doc_repo}
REPO_REMOTE=${REPO_REMOTE:-origin}
CARLA_REPO_DIR=${CARLA_REPO_DIR:-./temp/carla}
OUTPUT_DIR="${OUTPUT_DIR:-./dist}"
LOG_LEVEL="${LOG_LEVEL:-error}"
PYTHON_BIN="${PYTHON_BIN:-python}"

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

repo_checkout() {
    local dest=$1
    local remote=$2
    local branch=$3
    local url=$4
    local use_tag=${5:-0}
    local status
    if [ -d "$dest" ]; then
        if [ $use_tag -eq 1 ]; then
            info "switching $dest to tag $branch ..."
            git -C "$dest" fetch "$remote" --tags \
                && git -C "$dest" switch --detach -q "$branch"
            status=$?
        else
            info "switching $dest to branch $remote/$branch ..."
            git -C "$dest" remote set-branches --add "$remote" "$branch" \
                && git -C "$dest" fetch "$remote" \
                && git -C "$dest" switch -q "$branch"
            status=$?
        fi
    else
        info "cloning repo $dest"
        git clone -b "$branch" --depth=1 "$url" "$dest"
        status=$?
    fi
    if [ $status -ne 0 ]; then
        error "failed to checkout $dest, abort"
        clear_temp
        exit 1
    fi
}

checkout() {
    repo_checkout "$REPO_DIR" "$REPO_REMOTE" "$CARLA_VERSION" 'https://github.com/MamoruDS/carla-interface.git'
    repo_checkout "$CARLA_REPO_DIR" origin "$CARLA_VERSION" 'https://github.com/carla-simulator/carla.git' 1
    
    info 'copying PythonAPI docs ...'
    cp "$CARLA_REPO_DIR"/PythonAPI/docs/*.yml "$temp_doc_dir" 
}

generate_stub_files() {
    info 'generating stub files from docs ...'
    "$PYTHON_BIN" -m carla_doc \
                -l "$LOG_LEVEL" \
                -i "$temp_doc_dir" \
                --patches-root "$REPO_DIR/doc_patches" \
                --extra-root "$REPO_DIR/extra_docs" \
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
