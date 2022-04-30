```mermaid
erDiagram
  USER {
    string email
    string first_name
    string last_name
  }
  POST {
    text subject
    text body
  }
  COMMENT {
    text subject
    text content
  }

  USER ||--o{ POST : writes
  USER ||--o{ COMMENT : writes
  POST ||--o{ COMMENT : contains
  ```