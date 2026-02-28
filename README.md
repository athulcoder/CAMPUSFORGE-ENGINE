# CAMPUSFORGE-ENGINE


### ER - DIAGRAM
![alt text](docs/ER_diagram_CampusForge-Engine.png)



### FLOW 
```bash
Resume PDF
   ↓
PDF Parser (text only)
   ↓
Extractor (structured data)
   ↓
Normalizer (skills)
   ↓
Scoring Engine
   ↓
Redis (fast view) + DB (full data)

```

## INSTALLATION GUIDE

### prerequisites

Ensure that <b>git</b> and <b>docker</b> is installed in your system.

### Clone the repository:

```bash
git clone https://github.com/athulcoder/campusforge-engine
cd campus-forge-engine
```
#### ensure that the below ports are free
| Port | Used By       |
| ---- | ------------- |
| 3000 | Frontend      |
| 8080 | Backend       |
| 6379 | Redis         |
| 9000 | MinIO API     |
| 9001 | MinIO Console |

### Run docker compose
``` bash
docker compose up --build
```

#### frontend
Go to 
```
http://localhost:3000
```

## API documentation

The backend of this app runs on PORT 8080

### login
```
http://localhost:8080/api/auth/login
```
```json
{
   "email":"mail@email.com"
   "password":"123456"
}
```


### register
```
http://localhost:8080/api/auth/register
```
```json
{
   "name":"Paul Jacob",
   "email":"pauljacob@yahoo.com",
   "password":"123456"
}
```



### upload resume 
```
curl -X POST http://localhost:8080/api/resume/upload \
  -F "file=@resume.pdf"
```

### candidate routes

GIVES ALL
```
http://localhost:8080/api/candidate
```
 role based 
``` 
http://localhost:8080/api/candidate?role=React Developer
```

#### TO see the details of a particular candidate
``` 
http://localhost:8080/api/candidate<resume_id>
```
Example
``` 
http://localhost:8080/api/candidate/a4ef69e4-8c00-40b5-b854-46e8d9571ef6
```

