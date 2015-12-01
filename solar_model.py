# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    **rc** - расстояние до ц.м.сиситемы
    **rcx** - расстояние до ц.м.с. по оси х
    **rcy** - расстояние до ц.м.с. по оси у
    **mrcx(y)** - масса да на координату помноженная
    """

    body.Fx = body.Fy = 0
    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        body.Fx += body.m * obj.m * G * (body.x-obj.x) * (r)**-3
        body.Fy += body.m * obj.m * G * (body.y-obj.y) * (r)**-3


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx / body.m
    body.Vx += ax * dt
    body.x += Vx * dt + (ax / 2) * dt ** 2

    ay = body.Fy / body.m
    body.Vy += ay * dt
    body.y += Vy * dt + (ay / 2) * dt ** 2


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
