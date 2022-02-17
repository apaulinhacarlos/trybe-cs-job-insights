from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    unique_job_types = set(item["job_type"] for item in data)
    return list(unique_job_types)


def filter_by_job_type(jobs, job_type):
    jobs_filtered = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered.append(job)

    return jobs_filtered


def get_unique_industries(path):
    data = read(path)
    unique_industries = set(item["industry"] for item in data)
    result = (item for item in unique_industries if len(item) != 0)
    return list(result)


def filter_by_industry(jobs, industry):
    industry_filtered = []
    for job in jobs:
        if job["industry"] == industry:
            industry_filtered.append(job)

    return industry_filtered


def get_max_salary(path):
    data = read(path)
    max_salary = [
        int(item["max_salary"])
        for item in data
        if item["max_salary"].isdigit()
    ]

    return max(max_salary)


def get_min_salary(path):
    data = read(path)
    min_salary = [
        int(item["min_salary"])
        for item in data
        if item["min_salary"].isdigit()
    ]

    return min(min_salary)


# Parei aqui
def keys_in_the_dict(job):
    if "min_salary" not in job or "max_salary" not in job:
        return False


def is_number(job, salary):
    if not (
        isinstance(job["min_salary"], int)
        or isinstance(job["max_salary"], int)
        or isinstance(salary, int)
    ):
        return False


def range_is_valid(job):
    if job["min_salary"] > job["max_salary"]:
        return False


def matches_salary_range(job, salary):
    if not (
        keys_in_the_dict(job) or is_number(job, salary) or range_is_valid(job)
    ):
        raise ValueError

    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
