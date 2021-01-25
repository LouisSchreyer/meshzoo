from helpers import _get_signed_areas

import meshzoo


def test_disk():
    points, cells = meshzoo.disk(9, 8)
    assert len(points) == 325
    assert len(cells) == 576
    # meshzoo.save2d("4gon_disk.svg", points, cells)
    assert (_get_signed_areas(points.T, cells) > 0.0).all()


def test_disk_quad():
    points, cells = meshzoo.disk_quad(11)
    assert len(points) == 121
    assert len(cells) == 100


if __name__ == "__main__":
    test_disk_quad()
