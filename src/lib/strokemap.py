# This file is part of MyPaint.
# Copyright (C) 2009 by Martin Renold <martinxyz@gmx.ch>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

import time, struct
import zlib
from numpy import *
import mypaintlib

import tiledsurface, idletask
N = tiledsurface.N

tasks = idletask.Processor(max_pending=6)

class StrokeShape:
    """
    This class stores the shape of a stroke in as a 1-bit bitmap. The
    information is stored in compressed memory blocks of the size of a
    tile (for fast lookup).
    """
    def __init__(self):
        self.strokemap = {}

    def init_from_snapshots(self, snapshot_before, snapshot_after):
        assert not self.strokemap
        # extract the layer from each snapshot
        a, b = snapshot_before.tiledict, snapshot_after.tiledict
        # enumerate all tiles that have changed
        a_tiles = set(a.iteritems())
        b_tiles = set(b.iteritems())
        changes = a_tiles.symmetric_difference(b_tiles)
        tiles_modified = set([pos for pos, data in changes])

        # for each tile, calculate the exact difference (not now, later, when idle)
        queue = []
        for tx, ty in tiles_modified:
            def work(tx=tx, ty=ty):
                # get the pixel data to compare
                a_data = a.get((tx, ty), tiledsurface.transparent_tile).rgba
                b_data = b.get((tx, ty), tiledsurface.transparent_tile).rgba

                data = empty((N, N), 'uint8')
                mypaintlib.tile_perceptual_change_strokemap(a_data, b_data, data)

                data_compressed = zlib.compress(data.tostring())
                self.strokemap[tx, ty] = data_compressed

            tasks.add_work(work, weight=1.0/len(tiles_modified))

    def init_from_string(self, data, translate_x, translate_y):
        assert not self.strokemap
        assert translate_x % N == 0
        assert translate_y % N == 0
        translate_x /= N
        translate_y /= N
        while data:
            tx, ty, size = struct.unpack('>iiI', data[:3*4])
            compressed_bitmap = data[3*4:size+3*4]
            self.strokemap[tx + translate_x, ty + translate_y] = compressed_bitmap
            data = data[size+3*4:]

    def save_to_string(self, translate_x, translate_y):
        assert translate_x % N == 0
        assert translate_y % N == 0
        translate_x /= N
        translate_y /= N
        tasks.finish_all()
        data = ''
        for (tx, ty), compressed_bitmap in self.strokemap.iteritems():
            tx, ty = tx + translate_x, ty + translate_y
            data += struct.pack('>iiI', tx, ty, len(compressed_bitmap))
            data += compressed_bitmap
        return data

    def touches_pixel(self, x, y):
        tasks.finish_all()
        data = self.strokemap.get((x/N, y/N))
        if data:
            data = fromstring(zlib.decompress(data), dtype='uint8')
            data.shape = (N, N)
            return data[y%N, x%N]

    def render_overlay(self, layer):
        surf = layer._surface # FIXME: Don't touch inner details of layer
        tasks.finish_all()
        for (tx, ty), data in self.strokemap.iteritems():
            data = fromstring(zlib.decompress(data), dtype='uint8')
            data.shape = (N, N)
            rgba = surf.get_tile_memory(tx, ty, readonly=False)
            # neutral gray, 50% opaque
            rgba[:,:,3] = data.astype('uint16') * (1<<15)/2
            rgba[:,:,0] = rgba[:,:,3]/2
            rgba[:,:,1] = rgba[:,:,3]/2
            rgba[:,:,2] = rgba[:,:,3]/2


