# job_crawler

# LinkedIn Job and Profile Matcher

A Django-based system that crawls LinkedIn job postings and profiles, stores them in a database, and provides APIs for matching jobs and profiles based on various criteria.

## Setup and Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Start the server:
```bash
python manage.py runserver
```

## Architecture

The system consists of three main components:
1. Web Crawlers: Selenium-based scrapers for LinkedIn jobs and profiles
2. Database: SQLite (default Django database)
3. REST APIs: Django views serving JSON responses

### Database Schema

Two main models:
- JobPosting: Stores job listings with title, company, location, etc.
- Profile: Stores LinkedIn profiles with name, title, skills, etc.

### APIs

1. GET /api/profiles/
   - Input: designation, location, company
   - Output: List of matching profiles with match scores

2. GET /api/jobs/
   - Input: title, location, experience
   - Output: List of matching jobs with match scores

## Matching Algorithm

The current implementation uses a simple weighted scoring system:

### Profile Matching
- Title/Designation match: 40%
- Location match: 30%
- Company match: 30%

### Job Matching
- Title match: 50%
- Location match: 50%

Future improvements could include:
- Skills overlap analysis
- Experience level matching
- Industry relevance
- Keyword frequency analysis
- NLP-based similarity scoring

## Scalability Considerations

### Pros:
- Simple, easy to maintain architecture
- Basic caching can be implemented using Django's caching framework
- Easy to horizontally scale by adding more web servers

### Cons:
- Basic matching algorithm might not scale well for large datasets
- Single-threaded scraping might be slow for large number of profiles
- SQLite database might become a bottleneck (consider PostgreSQL for production)

## Limitations and Future Improvements

1. LinkedIn Rate Limiting:
   - Implement proper delays between requests
   - Add proxy rotation
   - Handle authentication properly

2. Data Quality:
   - Add data validation and cleaning
   - Implement better text parsing for skills and descriptions
   - Add regular data updates

3. Performance:
   - Add caching layer
   - Implement background job processing
   - Optimize database queries

## Notes

- This is a basic implementation that respects LinkedIn's robots.txt
- For production use, consider:
  - Adding proper authentication
  - Implementing rate limiting
  - Using a production-grade database
  - Adding logging and monitoring
  - Implementing proper error handling
