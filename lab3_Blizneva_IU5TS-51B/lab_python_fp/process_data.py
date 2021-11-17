import json
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique


path = 'data_light.json'
with open(path, encoding="utf-8") as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(list(Unique(list(field(arg, "job-name")), True)), key=lambda x: x.lower())


@print_result
def f2(arg):
    return list(filter(lambda x: x[:11].lower() == 'программист', arg))


@print_result
def f3(arg):
    return list(map(lambda x: x+' с опытом Python', arg))


@print_result
def f4(arg):
    salary = list(gen_random(len(arg), 100000, 200000))
    return ['{}, зарплата {} руб.'.format(job, salary) for job, salary in zip(arg, salary)]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))