#!/bin/bash
# Builds the Lambda dependency layer as layer.zip.
# Requires: Docker Desktop running.
#
# Usage (from project root):
#   bash lambda_layer/build_layer.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
LAYER_DIR="$SCRIPT_DIR"
ZIP_PATH="$LAYER_DIR/layer.zip"
PYTHON_DIR="$LAYER_DIR/python"

echo "==> Cleaning previous build..."
rm -rf "$PYTHON_DIR"
rm -f "$ZIP_PATH"

echo "==> Installing dependencies via Docker (Amazon Linux 2023 / Python 3.12)..."
docker run --rm \
  --platform linux/amd64 \
  -v "$PROJECT_DIR/lambda/requirements.txt:/requirements.txt:ro" \
  -v "$LAYER_DIR:/out" \
  public.ecr.aws/lambda/python:3.12 \
  /bin/bash -c "
    pip install -r /requirements.txt \
        --target /out/python \
        --platform manylinux2014_x86_64 \
        --implementation cp \
        --python-version 3.12 \
        --only-binary=:all: \
        --upgrade \
        --quiet
    echo 'pip install complete'
  "

echo "==> Creating layer.zip..."
cd "$LAYER_DIR"
zip -r9 layer.zip python/ --quiet

# Verify zip structure
echo "==> Verifying zip structure..."
TOP=$(unzip -l layer.zip | awk 'NR>3 && $NF != "" {print $NF}' | head -1 | cut -d'/' -f1)
if [ "$TOP" != "python" ]; then
  echo "ERROR: layer.zip top-level entry is '$TOP', expected 'python'."
  exit 1
fi

# Verify key packages
for PKG in requests bs4 gspread; do
  COUNT=$(unzip -l layer.zip "python/${PKG}/*" 2>/dev/null | grep -c "${PKG}" || true)
  if [ "$COUNT" -eq 0 ]; then
    echo "ERROR: package '${PKG}' not found in layer.zip."
    exit 1
  fi
  echo "  OK: ${PKG}"
done

SIZE=$(du -sh "$ZIP_PATH" | cut -f1)
echo ""
echo "Done: $ZIP_PATH ($SIZE)"
echo "Expected: ~10-15MB zipped."
