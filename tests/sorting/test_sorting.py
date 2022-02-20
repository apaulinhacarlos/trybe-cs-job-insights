from src.sorting import sort_by

fake_jobs = [
    {"min_salary": 3000, "max_salary": 4000, "date_posted": "2021-10-24"},
    {"min_salary": 8000, "max_salary": 10000, "date_posted": "2021-08-08"},
    {"min_salary": 4000, "max_salary": 8000, "date_posted": "2022-01-19"},
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2020-03-18"},
]

fake_jobs_min_salary = [
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2020-03-18"},
    {"min_salary": 3000, "max_salary": 4000, "date_posted": "2021-10-24"},
    {"min_salary": 4000, "max_salary": 8000, "date_posted": "2022-01-19"},
    {"min_salary": 8000, "max_salary": 10000, "date_posted": "2021-08-08"},
]

fake_jobs_max_salary = [
    {"min_salary": 8000, "max_salary": 10000, "date_posted": "2021-08-08"},
    {"min_salary": 4000, "max_salary": 8000, "date_posted": "2022-01-19"},
    {"min_salary": 3000, "max_salary": 4000, "date_posted": "2021-10-24"},
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2020-03-18"},
]

fake_jobs_date_posted = [
    {"min_salary": 4000, "max_salary": 8000, "date_posted": "2022-01-19"},
    {"min_salary": 3000, "max_salary": 4000, "date_posted": "2021-10-24"},
    {"min_salary": 8000, "max_salary": 10000, "date_posted": "2021-08-08"},
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2020-03-18"},
]


def test_sort_by_criteria():
    sort_by(fake_jobs, "min_salary")
    assert fake_jobs == fake_jobs_min_salary

    sort_by(fake_jobs, "max_salary")
    assert fake_jobs == fake_jobs_max_salary

    sort_by(fake_jobs, "date_posted")
    assert fake_jobs == fake_jobs_date_posted
