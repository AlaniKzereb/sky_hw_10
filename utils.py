import json
from classes import Candidate


def load_candidates(filename):
    """Загружает данные из файла"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def get_all(data):
    """Показывает всех кандидатов"""
    applicants = []
    for item in data:
        candidate = Candidate(item['pk'], item['name'], item['position'], item['skills'].lower(), item['picture'])
        applicants.append(candidate)
    return applicants


def get_by_pk(pk, data):
    """Возвращает кaндидатов по pk"""
    for item in data:
        if item.pk == pk:
            return item


def get_by_skill(skill_name, data):
    """Возвращает кандидатов по навыку"""
    arr = []
    for item in data:
        if skill_name in item.skills.split(','):
            arr.append(item)
    return arr
