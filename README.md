# CAMPUSFORGE-ENGINE


### ER - DIAGRAM
![alt text](docs/ER_diagram_CampusForge-Engine.png)


```bash
Resume PDF
   ↓
PDF Parser (text only)
   ↓
Extractor (structured data)
   ↓
Normalizer (skills, dates, roles)
   ↓
Scoring Engine
   ↓
Redis (fast view) + DB (full data)

```