# ROKEY-TA
두산로보틱스 Rokey9기 수료 후 TA 인턴 (2026.11.02 ~ )

## 자동 일일 업무 보고

GitHub Actions가 평일 18:00(한국 시간)에 기본 브랜치의 당일 커밋을 모아 `reports/daily/YYYY-MM-DD.md` 보고서를 생성하고, `daily-work-report/YYYY-MM-DD` 브랜치에 커밋한 뒤 PR을 생성하거나 기존 PR을 갱신합니다. 당일 커밋이 없으면 보고서와 PR을 만들지 않습니다. 예약 실행은 GitHub Actions 사정에 따라 지연될 수 있으며, `workflow_dispatch`로 수동 실행할 수도 있습니다.

보고서에는 당일 기본 브랜치에 푸시된 커밋 메시지와 변경 파일이 포함되므로, 업무 내용을 PR에 반영하려면 해당 커밋을 18:00 전에 기본 브랜치에 푸시해야 합니다. 워크플로가 PR을 생성할 수 있도록 저장소의 Actions 권한에서 `GITHUB_TOKEN`의 쓰기 권한을 허용해야 합니다.
