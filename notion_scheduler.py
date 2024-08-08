import os
import sys
import django
import json
import requests
from datetime import datetime
from pathlib import Path

# 프로젝트 루트 디렉토리 설정
BASE_DIR = Path(__file__).resolve().parent.parent

print(f"BASE_DIR: {BASE_DIR}")
print(f"BASE_DIR (absolute path): {BASE_DIR.absolute()}")
print(f"Current working directory: {os.getcwd()}")

# Django 프로젝트 경로 추가
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / 'mysite'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


# Django 설정
django.setup()

from pybo.models import ImageURL

# 설정 파일 로드
def load_config():
    config_path = 'secret_key.json'
    try:
        with open(config_path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        print(f"secret_key.json 파일을 찾을 수 없습니다. 경로: {config_path}")
        return None
    except json.JSONDecodeError:
        print("secret_key.json 파일의 형식이 올바르지 않습니다.")
        return None

# Notion API 설정
config = load_config()
if not config:
    raise SystemExit("설정을 불러올 수 없습니다. 프로그램을 종료합니다.")

NOTION_TOKEN = config.get('NOTION_TOKEN')
DATABASE_ID = config.get('NOTION_DATABASE_ID')
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

# 데이터베이스 쿼리 함수
def query_database():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    payload = {
        "sorts": [
            {
                "property": "Created time",
                "direction": "descending"
            }
        ],
        "page_size": 1
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        print(f"API 요청 실패. 상태 코드: {response.status_code}")
        print(f"응답 내용: {response.text}")
        return None

    return response.json()

# 페이지에서 텍스트 속성 추출 함수
def extract_text_property(page):
    properties = page['properties']
    for prop_name, prop_value in properties.items():
        if prop_value['type'] == 'rich_text':
            return prop_value['rich_text'][0]['plain_text'] if prop_value['rich_text'] else ""
    return ""

# 이미지 URL 업데이트 함수
def update_image_url():
    if not NOTION_TOKEN or not DATABASE_ID:
        print("NOTION_TOKEN 또는 NOTION_DATABASE_ID가 설정되지 않았습니다.")
        return

    result = query_database()

    if result is None:
        print("API 요청에 실패했습니다.")
        return

    if 'results' not in result or not result['results']:
        print("데이터베이스에서 항목을 찾을 수 없습니다.")
        return

    most_recent_page = result['results'][0]
    image_url = extract_text_property(most_recent_page)
    created_time = datetime.fromisoformat(most_recent_page['created_time'].rstrip('Z'))

    if image_url:
        # Django 데이터베이스 업데이트
        image_url_obj, created = ImageURL.objects.get_or_create(id=1)
        image_url_obj.url = image_url
        image_url_obj.save()

        print(f"\n이미지 URL이 업데이트되었습니다. (생성 시간: {created_time})")
        print(f"새 이미지 URL: {image_url}")
    else:
        print("이미지 URL을 찾을 수 없습니다.")

