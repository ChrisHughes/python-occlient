# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_mypaintlib', [dirname(__file__)])
        except ImportError:
            import _mypaintlib
            return _mypaintlib
        if fp is not None:
            try:
                _mod = imp.load_module('_mypaintlib', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _mypaintlib = swig_import_helper()
    del swig_import_helper
else:
    import _mypaintlib
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class Rect(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Rect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Rect, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _mypaintlib.Rect_x_set
    __swig_getmethods__["x"] = _mypaintlib.Rect_x_get
    if _newclass:x = _swig_property(_mypaintlib.Rect_x_get, _mypaintlib.Rect_x_set)
    __swig_setmethods__["y"] = _mypaintlib.Rect_y_set
    __swig_getmethods__["y"] = _mypaintlib.Rect_y_get
    if _newclass:y = _swig_property(_mypaintlib.Rect_y_get, _mypaintlib.Rect_y_set)
    __swig_setmethods__["w"] = _mypaintlib.Rect_w_set
    __swig_getmethods__["w"] = _mypaintlib.Rect_w_get
    if _newclass:w = _swig_property(_mypaintlib.Rect_w_get, _mypaintlib.Rect_w_set)
    __swig_setmethods__["h"] = _mypaintlib.Rect_h_set
    __swig_getmethods__["h"] = _mypaintlib.Rect_h_get
    if _newclass:h = _swig_property(_mypaintlib.Rect_h_get, _mypaintlib.Rect_h_set)
    def __init__(self): 
        this = _mypaintlib.new_Rect()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _mypaintlib.delete_Rect
Rect_swigregister = _mypaintlib.Rect_swigregister
Rect_swigregister(Rect)

class Surface(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Surface, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Surface, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _mypaintlib.delete_Surface
    def draw_dab(self, *args): return _mypaintlib.Surface_draw_dab(self, *args)
    def get_color(self, *args): return _mypaintlib.Surface_get_color(self, *args)
Surface_swigregister = _mypaintlib.Surface_swigregister
Surface_swigregister(Surface)

ACTUAL_RADIUS_MIN = _mypaintlib.ACTUAL_RADIUS_MIN
ACTUAL_RADIUS_MAX = _mypaintlib.ACTUAL_RADIUS_MAX
class Brush(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Brush, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Brush, name)
    __repr__ = _swig_repr
    __swig_setmethods__["print_inputs"] = _mypaintlib.Brush_print_inputs_set
    __swig_getmethods__["print_inputs"] = _mypaintlib.Brush_print_inputs_get
    if _newclass:print_inputs = _swig_property(_mypaintlib.Brush_print_inputs_get, _mypaintlib.Brush_print_inputs_set)
    __swig_setmethods__["stroke_total_painting_time"] = _mypaintlib.Brush_stroke_total_painting_time_set
    __swig_getmethods__["stroke_total_painting_time"] = _mypaintlib.Brush_stroke_total_painting_time_get
    if _newclass:stroke_total_painting_time = _swig_property(_mypaintlib.Brush_stroke_total_painting_time_get, _mypaintlib.Brush_stroke_total_painting_time_set)
    __swig_setmethods__["stroke_current_idling_time"] = _mypaintlib.Brush_stroke_current_idling_time_set
    __swig_getmethods__["stroke_current_idling_time"] = _mypaintlib.Brush_stroke_current_idling_time_get
    if _newclass:stroke_current_idling_time = _swig_property(_mypaintlib.Brush_stroke_current_idling_time_get, _mypaintlib.Brush_stroke_current_idling_time_set)
    def __init__(self): 
        this = _mypaintlib.new_Brush()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _mypaintlib.delete_Brush
    def reset(self): return _mypaintlib.Brush_reset(self)
    def new_stroke(self): return _mypaintlib.Brush_new_stroke(self)
    def set_base_value(self, *args): return _mypaintlib.Brush_set_base_value(self, *args)
    def set_mapping_n(self, *args): return _mypaintlib.Brush_set_mapping_n(self, *args)
    def set_mapping_point(self, *args): return _mypaintlib.Brush_set_mapping_point(self, *args)
    def get_state(self, *args): return _mypaintlib.Brush_get_state(self, *args)
    def set_state(self, *args): return _mypaintlib.Brush_set_state(self, *args)
    def stroke_to(self, *args): return _mypaintlib.Brush_stroke_to(self, *args)
Brush_swigregister = _mypaintlib.Brush_swigregister
Brush_swigregister(Brush)

class Mapping(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Mapping, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Mapping, name)
    __repr__ = _swig_repr
    __swig_setmethods__["base_value"] = _mypaintlib.Mapping_base_value_set
    __swig_getmethods__["base_value"] = _mypaintlib.Mapping_base_value_get
    if _newclass:base_value = _swig_property(_mypaintlib.Mapping_base_value_get, _mypaintlib.Mapping_base_value_set)
    def __init__(self, *args): 
        this = _mypaintlib.new_Mapping(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _mypaintlib.delete_Mapping
    def set_n(self, *args): return _mypaintlib.Mapping_set_n(self, *args)
    def set_point(self, *args): return _mypaintlib.Mapping_set_point(self, *args)
    def is_constant(self): return _mypaintlib.Mapping_is_constant(self)
    def calculate(self, *args): return _mypaintlib.Mapping_calculate(self, *args)
    def calculate_single_input(self, *args): return _mypaintlib.Mapping_calculate_single_input(self, *args)
Mapping_swigregister = _mypaintlib.Mapping_swigregister
Mapping_swigregister(Mapping)

class PythonBrush(Brush):
    __swig_setmethods__ = {}
    for _s in [Brush]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PythonBrush, name, value)
    __swig_getmethods__ = {}
    for _s in [Brush]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, PythonBrush, name)
    __repr__ = _swig_repr
    def python_get_state(self): return _mypaintlib.PythonBrush_python_get_state(self)
    def python_set_state(self, *args): return _mypaintlib.PythonBrush_python_set_state(self, *args)
    def python_stroke_to(self, *args): return _mypaintlib.PythonBrush_python_stroke_to(self, *args)
    def __init__(self): 
        this = _mypaintlib.new_PythonBrush()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _mypaintlib.delete_PythonBrush
PythonBrush_swigregister = _mypaintlib.PythonBrush_swigregister
PythonBrush_swigregister(PythonBrush)


def draw_dab_pixels_BlendMode_Normal(*args):
  return _mypaintlib.draw_dab_pixels_BlendMode_Normal(*args)
draw_dab_pixels_BlendMode_Normal = _mypaintlib.draw_dab_pixels_BlendMode_Normal

def draw_dab_pixels_BlendMode_Normal_and_Eraser(*args):
  return _mypaintlib.draw_dab_pixels_BlendMode_Normal_and_Eraser(*args)
draw_dab_pixels_BlendMode_Normal_and_Eraser = _mypaintlib.draw_dab_pixels_BlendMode_Normal_and_Eraser

def draw_dab_pixels_BlendMode_LockAlpha(*args):
  return _mypaintlib.draw_dab_pixels_BlendMode_LockAlpha(*args)
draw_dab_pixels_BlendMode_LockAlpha = _mypaintlib.draw_dab_pixels_BlendMode_LockAlpha

def get_color_pixels_accumulate(*args):
  return _mypaintlib.get_color_pixels_accumulate(*args)
get_color_pixels_accumulate = _mypaintlib.get_color_pixels_accumulate
TILE_SIZE = _mypaintlib.TILE_SIZE
MAX_MIPMAP_LEVEL = _mypaintlib.MAX_MIPMAP_LEVEL
class TiledSurface(Surface):
    __swig_setmethods__ = {}
    for _s in [Surface]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TiledSurface, name, value)
    __swig_getmethods__ = {}
    for _s in [Surface]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, TiledSurface, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _mypaintlib.new_TiledSurface(*args)
        try: self.this.append(this)
        except: self.this = this
    def begin_atomic(self): return _mypaintlib.TiledSurface_begin_atomic(self)
    def end_atomic(self): return _mypaintlib.TiledSurface_end_atomic(self)
    def get_tile_memory(self, *args): return _mypaintlib.TiledSurface_get_tile_memory(self, *args)
    def render_dab_mask(self, *args): return _mypaintlib.TiledSurface_render_dab_mask(self, *args)
    def draw_dab(self, *args): return _mypaintlib.TiledSurface_draw_dab(self, *args)
    def get_color(self, *args): return _mypaintlib.TiledSurface_get_color(self, *args)
    def get_alpha(self, *args): return _mypaintlib.TiledSurface_get_alpha(self, *args)
    __swig_destroy__ = _mypaintlib.delete_TiledSurface
TiledSurface_swigregister = _mypaintlib.TiledSurface_swigregister
TiledSurface_swigregister(TiledSurface)


def tile_downscale_rgb16(*args):
  return _mypaintlib.tile_downscale_rgb16(*args)
tile_downscale_rgb16 = _mypaintlib.tile_downscale_rgb16

def tile_downscale_rgba16(*args):
  return _mypaintlib.tile_downscale_rgba16(*args)
tile_downscale_rgba16 = _mypaintlib.tile_downscale_rgba16

def tile_composite_rgba16_over_rgb16(*args):
  return _mypaintlib.tile_composite_rgba16_over_rgb16(*args)
tile_composite_rgba16_over_rgb16 = _mypaintlib.tile_composite_rgba16_over_rgb16

def tile_composite_rgba16_multiply_rgb16(*args):
  return _mypaintlib.tile_composite_rgba16_multiply_rgb16(*args)
tile_composite_rgba16_multiply_rgb16 = _mypaintlib.tile_composite_rgba16_multiply_rgb16

def tile_composite_rgba16_screen_rgb16(*args):
  return _mypaintlib.tile_composite_rgba16_screen_rgb16(*args)
tile_composite_rgba16_screen_rgb16 = _mypaintlib.tile_composite_rgba16_screen_rgb16

def tile_composite_rgba16_dodge_rgb16(*args):
  return _mypaintlib.tile_composite_rgba16_dodge_rgb16(*args)
tile_composite_rgba16_dodge_rgb16 = _mypaintlib.tile_composite_rgba16_dodge_rgb16

def tile_composite_rgba16_burn_rgb16(*args):
  return _mypaintlib.tile_composite_rgba16_burn_rgb16(*args)
tile_composite_rgba16_burn_rgb16 = _mypaintlib.tile_composite_rgba16_burn_rgb16

def tile_blit_rgb16_into_rgb16(*args):
  return _mypaintlib.tile_blit_rgb16_into_rgb16(*args)
tile_blit_rgb16_into_rgb16 = _mypaintlib.tile_blit_rgb16_into_rgb16

def tile_clear(*args):
  return _mypaintlib.tile_clear(*args)
tile_clear = _mypaintlib.tile_clear

def precalculate_dithering_noise_if_required():
  return _mypaintlib.precalculate_dithering_noise_if_required()
precalculate_dithering_noise_if_required = _mypaintlib.precalculate_dithering_noise_if_required

def tile_convert_rgba16_to_rgba8(*args):
  return _mypaintlib.tile_convert_rgba16_to_rgba8(*args)
tile_convert_rgba16_to_rgba8 = _mypaintlib.tile_convert_rgba16_to_rgba8

def tile_convert_rgb16_to_rgb8(*args):
  return _mypaintlib.tile_convert_rgb16_to_rgb8(*args)
tile_convert_rgb16_to_rgb8 = _mypaintlib.tile_convert_rgb16_to_rgb8

def tile_convert_rgba8_to_rgba16(*args):
  return _mypaintlib.tile_convert_rgba8_to_rgba16(*args)
tile_convert_rgba8_to_rgba16 = _mypaintlib.tile_convert_rgba8_to_rgba16

def tile_perceptual_change_strokemap(*args):
  return _mypaintlib.tile_perceptual_change_strokemap(*args)
tile_perceptual_change_strokemap = _mypaintlib.tile_perceptual_change_strokemap
class SCWSColorSelector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SCWSColorSelector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SCWSColorSelector, name)
    __repr__ = _swig_repr
    def get_size(self): return _mypaintlib.SCWSColorSelector_get_size(self)
    __swig_setmethods__["brush_h"] = _mypaintlib.SCWSColorSelector_brush_h_set
    __swig_getmethods__["brush_h"] = _mypaintlib.SCWSColorSelector_brush_h_get
    if _newclass:brush_h = _swig_property(_mypaintlib.SCWSColorSelector_brush_h_get, _mypaintlib.SCWSColorSelector_brush_h_set)
    __swig_setmethods__["brush_s"] = _mypaintlib.SCWSColorSelector_brush_s_set
    __swig_getmethods__["brush_s"] = _mypaintlib.SCWSColorSelector_brush_s_get
    if _newclass:brush_s = _swig_property(_mypaintlib.SCWSColorSelector_brush_s_get, _mypaintlib.SCWSColorSelector_brush_s_set)
    __swig_setmethods__["brush_v"] = _mypaintlib.SCWSColorSelector_brush_v_set
    __swig_getmethods__["brush_v"] = _mypaintlib.SCWSColorSelector_brush_v_get
    if _newclass:brush_v = _swig_property(_mypaintlib.SCWSColorSelector_brush_v_get, _mypaintlib.SCWSColorSelector_brush_v_set)
    def set_brush_color(self, *args): return _mypaintlib.SCWSColorSelector_set_brush_color(self, *args)
    def get_hsva_at(self, *args): return _mypaintlib.SCWSColorSelector_get_hsva_at(self, *args)
    def pick_color_at(self, *args): return _mypaintlib.SCWSColorSelector_pick_color_at(self, *args)
    def render(self, *args): return _mypaintlib.SCWSColorSelector_render(self, *args)
    def __init__(self): 
        this = _mypaintlib.new_SCWSColorSelector()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _mypaintlib.delete_SCWSColorSelector
SCWSColorSelector_swigregister = _mypaintlib.SCWSColorSelector_swigregister
SCWSColorSelector_swigregister(SCWSColorSelector)
cvar = _mypaintlib.cvar
dithering_noise_size = cvar.dithering_noise_size
colorring_size = cvar.colorring_size
center = cvar.center
RAD_TO_ONE = cvar.RAD_TO_ONE
TWO_PI = cvar.TWO_PI
ONE_OVER_THREE = cvar.ONE_OVER_THREE
TWO_OVER_THREE = cvar.TWO_OVER_THREE

class ColorChangerWash(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ColorChangerWash, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ColorChangerWash, name)
    __repr__ = _swig_repr
    __swig_setmethods__["brush_h"] = _mypaintlib.ColorChangerWash_brush_h_set
    __swig_getmethods__["brush_h"] = _mypaintlib.ColorChangerWash_brush_h_get
    if _newclass:brush_h = _swig_property(_mypaintlib.ColorChangerWash_brush_h_get, _mypaintlib.ColorChangerWash_brush_h_set)
    __swig_setmethods__["brush_s"] = _mypaintlib.ColorChangerWash_brush_s_set
    __swig_getmethods__["brush_s"] = _mypaintlib.ColorChangerWash_brush_s_get
    if _newclass:brush_s = _swig_property(_mypaintlib.ColorChangerWash_brush_s_get, _mypaintlib.ColorChangerWash_brush_s_set)
    __swig_setmethods__["brush_v"] = _mypaintlib.ColorChangerWash_brush_v_set
    __swig_getmethods__["brush_v"] = _mypaintlib.ColorChangerWash_brush_v_get
    if _newclass:brush_v = _swig_property(_mypaintlib.ColorChangerWash_brush_v_get, _mypaintlib.ColorChangerWash_brush_v_set)
    def set_brush_color(self, *args): return _mypaintlib.ColorChangerWash_set_brush_color(self, *args)
    def get_size(self): return _mypaintlib.ColorChangerWash_get_size(self)
    def render(self, *args): return _mypaintlib.ColorChangerWash_render(self, *args)
    def pick_color_at(self, *args): return _mypaintlib.ColorChangerWash_pick_color_at(self, *args)
    def __init__(self): 
        this = _mypaintlib.new_ColorChangerWash()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _mypaintlib.delete_ColorChangerWash
ColorChangerWash_swigregister = _mypaintlib.ColorChangerWash_swigregister
ColorChangerWash_swigregister(ColorChangerWash)
ccw_size = cvar.ccw_size
v06_colorchanger = cvar.v06_colorchanger

class ColorChangerCrossedBowl(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ColorChangerCrossedBowl, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ColorChangerCrossedBowl, name)
    __repr__ = _swig_repr
    __swig_setmethods__["brush_h"] = _mypaintlib.ColorChangerCrossedBowl_brush_h_set
    __swig_getmethods__["brush_h"] = _mypaintlib.ColorChangerCrossedBowl_brush_h_get
    if _newclass:brush_h = _swig_property(_mypaintlib.ColorChangerCrossedBowl_brush_h_get, _mypaintlib.ColorChangerCrossedBowl_brush_h_set)
    __swig_setmethods__["brush_s"] = _mypaintlib.ColorChangerCrossedBowl_brush_s_set
    __swig_getmethods__["brush_s"] = _mypaintlib.ColorChangerCrossedBowl_brush_s_get
    if _newclass:brush_s = _swig_property(_mypaintlib.ColorChangerCrossedBowl_brush_s_get, _mypaintlib.ColorChangerCrossedBowl_brush_s_set)
    __swig_setmethods__["brush_v"] = _mypaintlib.ColorChangerCrossedBowl_brush_v_set
    __swig_getmethods__["brush_v"] = _mypaintlib.ColorChangerCrossedBowl_brush_v_get
    if _newclass:brush_v = _swig_property(_mypaintlib.ColorChangerCrossedBowl_brush_v_get, _mypaintlib.ColorChangerCrossedBowl_brush_v_set)
    def set_brush_color(self, *args): return _mypaintlib.ColorChangerCrossedBowl_set_brush_color(self, *args)
    def get_size(self): return _mypaintlib.ColorChangerCrossedBowl_get_size(self)
    def render(self, *args): return _mypaintlib.ColorChangerCrossedBowl_render(self, *args)
    def pick_color_at(self, *args): return _mypaintlib.ColorChangerCrossedBowl_pick_color_at(self, *args)
    def __init__(self): 
        this = _mypaintlib.new_ColorChangerCrossedBowl()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _mypaintlib.delete_ColorChangerCrossedBowl
ColorChangerCrossedBowl_swigregister = _mypaintlib.ColorChangerCrossedBowl_swigregister
ColorChangerCrossedBowl_swigregister(ColorChangerCrossedBowl)
ccdb_size = cvar.ccdb_size


def save_png_fast_progressive(*args):
  return _mypaintlib.save_png_fast_progressive(*args)
save_png_fast_progressive = _mypaintlib.save_png_fast_progressive

def gdkpixbuf_numeric2numpy(*args):
  return _mypaintlib.gdkpixbuf_numeric2numpy(*args)
gdkpixbuf_numeric2numpy = _mypaintlib.gdkpixbuf_numeric2numpy

