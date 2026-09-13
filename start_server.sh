#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE_DIR="$DIR/persian-book/site"
PORT=8000

echo "=== بازسازی صفحات سایت فارسی LPIC-1 ==="
python3 "$DIR/build.py"

echo ""
echo "=========================================================="
echo "  کتاب فارسی و راست‌چین LPIC-1 جادی آماده است!"
echo "  آدرس مشاهده آنلاین در مرورگر: http://localhost:$PORT"
echo "  همچنین فایل مستقیم: file://$SITE_DIR/index.html"
echo "=========================================================="
echo "سرور محلی در حال اجراست... (برای توقف کلیدهای Ctrl+C را فشار دهید)"

# Try opening in default browser if desktop is active
if command -v xdg-open > /dev/null 2>&1 && [ -n "$DISPLAY" ]; then
    (sleep 1 && xdg-open "http://localhost:$PORT") &
fi

cd "$SITE_DIR"
exec python3 -m http.server $PORT
