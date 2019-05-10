# -*- coding:utf-8 -*-


class Job(object):
    def __init__(self, info):
        self.category = info['category']
        self.company = info['company']
        self.job = info['job']
        self.location = info['location']
        self.experience = info['experience']
        self.education = info['education']
        self.salary = info['salary']
        self.hr = info['hr']
        self.description = info['description']

    def keys(self):
        return ('category', 'company', 'job',
                'location', 'experience', 'education',
                'salary', 'hr', 'description')

    def __getitem__(self, item):
        return getattr(self, item)
