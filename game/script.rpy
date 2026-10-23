## =============================================================================
##  QUICK SETTINGS
## =============================================================================

## TYPEWRITER MODE
##   True  = text types out letter by letter. Clicking while it types finishes
##           the line instantly; clicking again moves on to the next line.
##   False = Ren'Py's normal behavior (follows the player's Text Speed setting).
define -2 kt_typewriter = True

## Letters per second when typewriter mode is on.
define -2 kt_typewriter_cps = 40

## Show a blinking arrow at the end of a line once it has finished typing.
define -2 kt_show_ctc = True

## Seconds to pause after . , ! ? ; : and "..." while typing. 0 = off.
## (Can also be changed mid-game:  $ kt_punct_pause = 0.2 )
default kt_punct_pause = 0


################################################################################
##
##  ADVANCED GAME TEMPLATE  -  script.rpy
##
##  Put this file in your project's  game/  folder (replacing script.rpy), and
##  bg plaza.png in  game/images/  ->  scene bg plaza
##  Built for Ren'Py 8.5 (uses the default GL2 renderer and custom shaders).
##
##  Everything is prefixed with  kt_ / KT  so it won't clash with your code.
##  The story of Verity starts at the "STORY" section near the bottom.
##
################################################################################
##
##  1. TEXT EFFECTS
##  ---------------
##  Parameters go after "=", separated by commas, by name ("speed=2,radius=3")
##  or by position in the order listed ("2,3"), or mixed. Missing ones use
##  the defaults shown. Every tag works on a whole line or any part of one,
##  and tags can be nested:  {tempting}so {irritated}very{/irritated} tired{/tempting}
##
##  Every animated tag also accepts  color=#hex  and  style=some_text_style.
##
##  LOOPING MOTION
##    {shaky}      orbit around own center    speed=1.5 radius=2 phase=2.4
##    {irritated}  each letter jitters        intensity=2 speed=30
##    {tempting}   sine wave (Y)              speed=0.8 phase=0.45 amplitude=4
##    {sway}       sine wave (X)              speed=0.8 amplitude=3 phase=0.4
##    {bounce}     letters hop in a wave      speed=1 height=6 phase=0.35
##    {levitate}   each letter floats freely  speed=0.35 amplitude=4
##    {swing}      rock back and forth        speed=1 angle=12 phase=0.5
##    {spin}       spin continuously          speed=0.5 phase=0.3
##    {drunk}      woozy sway and tilt        speed=0.5 sway=3 angle=6 phase=0.6
##    {shiver}     fast sideways tremble      intensity=1 speed=45
##    {pulse}      grow and shrink            speed=1 amount=0.15 phase=0.5
##    {jelly}      squash and stretch         speed=1.2 amount=0.18 phase=0.5
##    {heartbeat}  "ba-dum" double pulse      speed=1.1 amount=0.25
##
##  LIGHT & COLOR
##    {flicker}    dying light bulb           speed=12 min=0.25
##    {ghost}      fade in and out in a wave  speed=0.6 min=0.15 phase=0.4
##    {blink}      on / off                   speed=1.2 duty=0.65 phase=0
##    {rainbow}    hue cycle                  speed=0.4 spread=0.06 saturation=0.6 value=1
##    {colorwave}  cycle through your colors  colors=#ff2d75|#ffd23f|#3fd2ff speed=0.5 spread=0.08
##    {glitch}     corrupt, jump, recolor     chance=0.08 speed=12 offset=4
##    {gradient=#c1,#c2,...}   static gradient (works with everything)
##    {red} {orange} {yellow} {green} {cyan} {blue} {purple} {pink} {gold} {gray}
##
##  ENTRANCES  (play as each letter is typed; stagger=0.05 cascades them
##              even when the text isn't typed out, e.g. menus / screens)
##    {fadein}     fade in and rise           duration=0.35 rise=10 stagger=0
##    {pop}        pop with overshoot         duration=0.3 stagger=0
##    {drop}       fall in and bounce         duration=0.5 height=30 stagger=0
##    {slidein}    slide in from the left     duration=0.35 distance=25 stagger=0
##    {zoomin}     shrink into place          duration=0.3 scale=2.5 stagger=0
##    {spinin}     spin and grow into place   duration=0.5 stagger=0
##    {spiral}     spiral into place          duration=0.6 radius=40 turns=1 stagger=0
##    {flip}       flip in like a card        duration=0.4 stagger=0
##    {impact}     slam in and shake          duration=0.45 scale=2.2 shake=4 stagger=0
##    {scramble}   decode from random symbols duration=0.6 speed=20 stagger=0
##
##  EXITS
##    {shatter}    letters burst apart and fall  delay=1.2 force=140 gravity=500 spin=360
##
##  PRESETS  (add your own with kt_preset in section 3)
##    {angry} {scared} {dreamy} {whisper} {shout} {hacker} {cursed} {love}
##    {fire} {ice} {neon} {spooky} {boss} {crumble}
##
##  TYPING SPEED  (typewriter mode)
##    {slow}..{/slow}  {quick}..{/quick}  built-in: {cps=*0.5} {w} {w=1.0} {p} {nw} {fast}
##    KTCharacter("Name", cps=20)   -> a character who always talks at that speed
##
##  WHOLE LINES / CHARACTERS
##    Character(..., what_color="#hex")                 colored sentences
##    KTCharacter("Name", effect="tempting=speed=0.6")  every line animated
##    KTCharacter(..., callback=kt_blip("audio/blip.ogg"))  typing sounds
##
##  2. THE STAGE
##  ------------
##  SPRITE TRANSFORMS   show verity normal at kt_stage, kt_float
##    kt_stage(x)  kt_float  kt_hop  kt_squash  kt_shake  kt_tremble  kt_nod
##    kt_breathe  kt_glow  kt_ghostly  kt_silhouette  kt_spin_in  kt_focus
##    kt_flip  kt_slide_in_left  kt_slide_in_right  kt_dim  kt_undim
##
##  TIME OF DAY (on a background)   scene bg plaza at kt_night
##    kt_day  kt_evening  kt_night  kt_dawn
##
##  WEATHER   show kt_rain  /  hide kt_rain
##    kt_rain  kt_storm  kt_snow  kt_petals  kt_embers  kt_fireflies  kt_dust
##    $ kt_lightning()
##
##  3. CAMERA  (python, use with $; filters stack and stay until reset)
##  ---------
##    kt_screen_shake(strength, duration)    kt_zoom_punch(amount)
##    kt_camera(filter, filter, ...)          kt_camera_reset()
##    Color filters:  kt_grayscale  kt_sepia  kt_nightmare  kt_invert
##                    kt_night  kt_evening  kt_day  kt_dawn  kt_blur(6)  kt_woozy
##    Shaders:        kt_crt  kt_vhs  kt_chroma(4)  kt_haze  kt_underwater
##                    kt_pixelate(10)  kt_bloom  kt_grain  kt_vignette  kt_screenglitch
##
##  4. EXTRAS
##  ---------
##    call kt_chapter("Chapter 1", "The Beginning")      chapter title card
##    transitions:  kt_flash  kt_red_flash  kt_blackout  kt_pixel  kt_quick
##
##  NOTES
##    - Animated letters use the style  kt_letter  (a copy of say_dialogue).
##      Style tags OUTSIDE an animated tag don't reach its letters: write
##      {shaky}{color=#f00}text{/color}{/shaky}  or  {shaky=color=#f00}text{/shaky}
##    - {rainbow}, {colorwave} and {glitch} tint the letters, so they look
##      best on white text (the default).
##    - Words stay together when wrapping, unless a tag starts or ends in the
##      middle of a word.
##
################################################################################


################################################################################
## ENGINE  (you shouldn't need to edit this section)
################################################################################

init -10 python:

    import math
    import random
    import re as _kt_re

    # Zero-width characters that control line breaking between animated
    # letters: WORD JOINER keeps a word together, ZERO WIDTH SPACE restores a
    # normal break opportunity at the end of a word.
    KT_WJ = "⁠"
    KT_ZW = "​"

    # Built-in style tags that are copied into every animated letter.
    KT_STYLE_TAGS = set([ "b", "i", "u", "s", "plain", "color", "size", "font",
                          "alpha", "k", "outlinecolor" ])

    kt_letter_style = "kt_letter"

    TAU = 2.0 * math.pi


    ## Parameters ------------------------------------------------------------

    def _kt_value(v):
        v = v.strip()
        try:
            return float(v)
        except Exception:
            return v

    def kt_parse(value, order, defaults):
        """
        Parses a tag value such as "speed=2,radius=3" or "2,3" into a dict.
        A bare value goes to the parameter at that position.
        """

        rv = dict(defaults)

        if not value:
            return rv

        for pos, item in enumerate(value.split(",")):
            if "=" in item:
                k, _, v = item.partition("=")
                rv[k.strip()] = _kt_value(v)
            elif item.strip() and pos < len(order):
                rv[order[pos]] = _kt_value(item)

        return rv


    ## Letters ---------------------------------------------------------------

    class KTState(object):
        """
        Everything the effects on one letter want to do this frame.
        """

        def __init__(self):
            self.dx = 0.0
            self.dy = 0.0
            self.rotate = 0.0
            self.zoom = 1.0
            self.xzoom = 1.0
            self.yzoom = 1.0
            self.alpha = 1.0
            self.tint = None
            self.char = None      # show a different character this frame


    class KTLetter(renpy.Displayable):
        """
        A single animated character placed inline in a Text.
        """

        def __init__(self, char, open_tags, close_tags, style, **kwargs):
            super(KTLetter, self).__init__(**kwargs)

            self.char = char
            self.open_tags = open_tags
            self.close_tags = close_tags
            self.text_style = style
            self.color = None
            self.effects = [ ]
            self._children = { }

        def set_color(self, color):
            self.color = color
            self._children = { }

        def set_style(self, style):
            self.text_style = style
            self._children = { }

        def add_effect(self, fn, params, index):
            self.effects.append((fn, params, index))

        def get_child(self, char=None):
            if char is None:
                char = self.char

            rv = self._children.get(char, None)

            if rv is None:
                ch = "{{" if char == "{" else char
                s = self.open_tags + ch + self.close_tags

                if self.color:
                    s = "{color=%s}%s{/color}" % (self.color, s)

                # slow=False: the letter must never type itself out; the
                # dialogue around it handles the typewriter timing.
                rv = Text(s, style=self.text_style, substitute=False, slow=False)

                if len(self._children) > 24:
                    self._children = { }

                self._children[char] = rv

            return rv

        def render(self, width, height, st, at):
            base = self.get_child()

            # The size always comes from the real character, so animation
            # never changes the layout of the line.
            cr = renpy.render(base, 4000, 4000, st, at)
            cw, ch = cr.get_size()

            s = KTState()
            redraw = False

            for fn, params, index in self.effects:
                if fn(params, index, st, at, s):
                    redraw = True

            child = base

            if s.char is not None and s.char != self.char:
                child = self.get_child(s.char)
                cr = renpy.render(child, 4000, 4000, st, at)

            if (s.rotate or s.zoom != 1.0 or s.xzoom != 1.0 or s.yzoom != 1.0
                    or s.alpha != 1.0 or s.tint is not None):

                xz = s.xzoom if abs(s.xzoom) > 0.01 else 0.01
                yz = s.yzoom if abs(s.yzoom) > 0.01 else 0.01

                t = Transform(
                    child,
                    rotate=(s.rotate or None),
                    zoom=max(0.01, s.zoom),
                    xzoom=xz,
                    yzoom=yz,
                    alpha=max(0.0, min(1.0, s.alpha)),
                    matrixcolor=(TintMatrix(s.tint) if s.tint is not None else None),
                    )
                cr = renpy.render(t, 4000, 4000, st, at)

            tw, th = cr.get_size()

            rv = renpy.Render(cw, ch)
            rv.subpixel_blit(cr, ((cw - tw) / 2.0 + s.dx, (ch - th) / 2.0 + s.dy))

            if redraw:
                renpy.redraw(self, 0)

            return rv

        def visit(self):
            return [ self.get_child() ]


    def _kt_apply(contents, fn, params):
        """
        Turns the characters inside a tag into KTLetters carrying `fn`. If the
        letters already exist (nested tags), just adds `fn` to them.
        """

        color = params.get("color", None)
        style = params.get("style", None)

        convert = False

        for kind, text in contents:
            if kind == renpy.TEXT_TEXT and text.strip(KT_WJ + KT_ZW + " \t\n　"):
                convert = True
                break

        # Nested inside another animated tag: the letters already exist.
        if not convert:
            index = 0

            for kind, text in contents:
                if kind == renpy.TEXT_DISPLAYABLE and isinstance(text, KTLetter):
                    text.add_effect(fn, params, index)
                    if color:
                        text.set_color(color)
                    if style:
                        text.set_style(style)
                    index += 1

            return contents

        rv = [ ]
        stack = [ ]
        index = 0
        prev_letter = False

        def joiner(ch):
            # cps=0 so the invisible joiner doesn't slow down the typewriter.
            rv.append((renpy.TEXT_TAG, "cps=0"))
            rv.append((renpy.TEXT_TEXT, ch))
            rv.append((renpy.TEXT_TAG, "/cps"))

        for kind, text in contents:

            if kind == renpy.TEXT_TEXT:
                for ch in text:

                    if ch == KT_WJ or ch == KT_ZW:
                        continue

                    if ch.isspace():
                        if prev_letter:
                            joiner(KT_ZW)
                        rv.append((renpy.TEXT_TEXT, ch))
                        prev_letter = False
                        continue

                    if prev_letter:
                        joiner(KT_WJ)

                    open_tags = "".join("{%s}" % t for t in stack)
                    close_tags = "".join("{/%s}" % t.partition("=")[0] for t in reversed(stack))

                    letter = KTLetter(ch, open_tags, close_tags, style or kt_letter_style)

                    if color:
                        letter.set_color(color)

                    letter.add_effect(fn, params, index)
                    index += 1

                    rv.append((renpy.TEXT_DISPLAYABLE, letter))
                    prev_letter = True

            elif kind == renpy.TEXT_TAG:
                name = text.partition("=")[0]

                if name.startswith("/"):
                    base = name[1:]
                    if base in KT_STYLE_TAGS:
                        for j in range(len(stack) - 1, -1, -1):
                            if stack[j].partition("=")[0] == base:
                                del stack[j]
                                break

                elif name in KT_STYLE_TAGS:
                    stack.append(text)

                # Every tag is passed through, so {w}, {nw}, {cps}, nested
                # animated tags and the rest keep working.
                rv.append((kind, text))

            else:
                rv.append((kind, text))
                prev_letter = False

        if prev_letter:
            joiner(KT_ZW)

        return rv


    KT_EFFECTS = { }

    def kt_register_effect(name, fn, order, defaults):
        """
        Registers a new animated text tag {name}.

        `fn(params, index, st, at, state)` runs every frame for every letter.
        `index` is the letter's position in the tag, `st` the time since that
        letter appeared, `at` a clock shared by all letters. Change `state`
        (dx, dy, rotate, zoom, xzoom, yzoom, alpha, tint, char) and return
        True while the letter still needs to animate.
        """

        defaults = dict(defaults)
        defaults.setdefault("color", None)
        defaults.setdefault("style", None)

        def tag_function(tag, value, contents):
            params = kt_parse(value, order, defaults)
            return _kt_apply(contents, fn, params)

        KT_EFFECTS[name] = (fn, order, defaults)
        config.custom_text_tags[name] = tag_function


    ## Helpers for effects -----------------------------------------------------

    def _kt_rng(*seed):
        h = 17
        for s in seed:
            h = (h * 1000003 + int(s)) & 0x7fffffff
        return random.Random(h)

    def _kt_wave(p, i, at):
        return math.sin(TAU * p["speed"] * at - i * p["phase"])

    def _kt_progress(p, i, st):
        """
        0 -> 1 progress of an entrance. Negative while the letter waits for
        its `stagger` delay.
        """
        return (st - i * p.get("stagger", 0.0)) / max(0.001, p["duration"])

    def _kt_ease_out_cubic(t):
        return 1.0 - (1.0 - t) ** 3

    def _kt_ease_out_bounce(t):
        n1, d1 = 7.5625, 2.75
        if t < 1 / d1:
            return n1 * t * t
        elif t < 2 / d1:
            t -= 1.5 / d1
            return n1 * t * t + 0.75
        elif t < 2.5 / d1:
            t -= 2.25 / d1
            return n1 * t * t + 0.9375
        else:
            t -= 2.625 / d1
            return n1 * t * t + 0.984375

    def _kt_entrance(fn):
        """
        Wraps an entrance effect: hides the letter while it waits, and stops
        animating once it's done.
        """

        def wrapper(p, i, st, at, s):
            t = _kt_progress(p, i, st)
            if t < 0.0:
                s.alpha = 0.0
                return True
            if t >= 1.0:
                return False
            fn(p, i, t, st, at, s)
            return True

        return wrapper


    ## Looping motion ---------------------------------------------------------

    def _kt_fx_shaky(p, i, st, at, s):
        a = TAU * p["speed"] * at + i * p["phase"]
        s.dx += math.cos(a) * p["radius"]
        s.dy += math.sin(a) * p["radius"]
        return True

    def _kt_fx_irritated(p, i, st, at, s):
        r = _kt_rng(i, at * p["speed"], 1)
        k = p["intensity"]
        s.dx += r.uniform(-k, k)
        s.dy += r.uniform(-k, k)
        return True

    def _kt_fx_tempting(p, i, st, at, s):
        s.dy += p["amplitude"] * _kt_wave(p, i, at)
        return True

    def _kt_fx_sway(p, i, st, at, s):
        s.dx += p["amplitude"] * _kt_wave(p, i, at)
        return True

    def _kt_fx_bounce(p, i, st, at, s):
        s.dy -= p["height"] * abs(math.sin(math.pi * p["speed"] * at - i * p["phase"]))
        return True

    def _kt_fx_levitate(p, i, st, at, s):
        r = _kt_rng(i, 7)
        f = 0.75 + 0.5 * r.random()
        s.dy += p["amplitude"] * math.sin(TAU * p["speed"] * f * at + r.random() * TAU)
        s.dx += p["amplitude"] * 0.35 * math.cos(TAU * p["speed"] * 0.6 * f * at + r.random() * TAU)
        return True

    def _kt_fx_swing(p, i, st, at, s):
        s.rotate += p["angle"] * _kt_wave(p, i, at)
        return True

    def _kt_fx_spin(p, i, st, at, s):
        s.rotate += (360.0 * p["speed"] * at + math.degrees(i * p["phase"])) % 360.0
        return True

    def _kt_fx_drunk(p, i, st, at, s):
        a = TAU * p["speed"] * at - i * p["phase"]
        s.dx += p["sway"] * math.sin(a)
        s.dy += p["sway"] * 0.5 * math.sin(a * 2.0)
        s.rotate += p["angle"] * math.sin(a + 0.8)
        return True

    def _kt_fx_shiver(p, i, st, at, s):
        r = _kt_rng(i, at * p["speed"], 2)
        s.dx += r.uniform(-p["intensity"], p["intensity"])
        return True

    def _kt_fx_pulse(p, i, st, at, s):
        s.zoom *= 1.0 + p["amount"] * _kt_wave(p, i, at)
        return True

    def _kt_fx_jelly(p, i, st, at, s):
        k = p["amount"] * _kt_wave(p, i, at)
        s.xzoom *= 1.0 + k
        s.yzoom *= 1.0 - k
        return True

    def _kt_fx_heartbeat(p, i, st, at, s):
        x = (at * p["speed"]) % 1.0
        beat = math.exp(-((x / 0.06) ** 2)) + 0.6 * math.exp(-(((x - 0.2) / 0.06) ** 2))
        s.zoom *= 1.0 + p["amount"] * beat
        return True


    ## Light & color ----------------------------------------------------------

    KT_GLITCH_CHARS = "#$%&@!?/\\|<>=+*~^"
    KT_GLITCH_COLORS = [ "#ff2a6d", "#05d9e8", "#d1f7ff", "#b967ff" ]

    def _kt_fx_flicker(p, i, st, at, s):
        r = _kt_rng(i, at * p["speed"], 3)
        s.alpha *= r.uniform(p["min"], 1.0)
        return True

    def _kt_fx_ghost(p, i, st, at, s):
        w = 0.5 + 0.5 * _kt_wave(p, i, at)
        s.alpha *= p["min"] + (1.0 - p["min"]) * w
        return True

    def _kt_fx_blink(p, i, st, at, s):
        c = (at * p["speed"] - i * p["phase"]) % 1.0
        if c > p["duty"]:
            s.alpha *= 0.12
        return True

    def _kt_fx_rainbow(p, i, st, at, s):
        h = (at * p["speed"] + i * p["spread"]) % 1.0
        s.tint = Color(hsv=(h, p["saturation"], p["value"]))
        return True

    def _kt_fx_colorwave(p, i, st, at, s):
        cols = p.get("_cols", None)
        if cols is None:
            cols = [ Color(c.strip()) for c in str(p["colors"]).split("|") if c.strip() ]
            p["_cols"] = cols
        if len(cols) == 1:
            s.tint = cols[0]
            return False
        x = (at * p["speed"] + i * p["spread"]) % 1.0 * len(cols)
        k = int(x)
        s.tint = cols[k % len(cols)].interpolate(cols[(k + 1) % len(cols)], x - k)
        return True

    def _kt_fx_glitch(p, i, st, at, s):
        r = _kt_rng(i, at * p["speed"], 4)
        if r.random() < p["chance"]:
            s.char = r.choice(KT_GLITCH_CHARS)
            s.dx += r.uniform(-p["offset"], p["offset"])
            s.dy += r.uniform(-p["offset"], p["offset"]) * 0.5
            s.tint = r.choice(KT_GLITCH_COLORS)
        return True


    ## Entrances ---------------------------------------------------------------

    KT_SCRAMBLE_CHARS = "!<>-_/\\[]=+*^?#$%&ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def _kt_fx_fadein(p, i, t, st, at, s):
        s.alpha *= t
        s.dy += (1.0 - _kt_ease_out_cubic(t)) * p["rise"]

    def _kt_fx_pop(p, i, t, st, at, s):
        c1 = 1.70158
        s.zoom *= 1.0 + (c1 + 1.0) * (t - 1.0) ** 3 + c1 * (t - 1.0) ** 2
        s.alpha *= min(1.0, t * 4.0)

    def _kt_fx_drop(p, i, t, st, at, s):
        s.dy -= (1.0 - _kt_ease_out_bounce(t)) * p["height"]
        s.alpha *= min(1.0, t * 4.0)

    def _kt_fx_slidein(p, i, t, st, at, s):
        s.dx -= (1.0 - _kt_ease_out_cubic(t)) * p["distance"]
        s.alpha *= t

    def _kt_fx_zoomin(p, i, t, st, at, s):
        e = _kt_ease_out_cubic(t)
        s.zoom *= p["scale"] + (1.0 - p["scale"]) * e
        s.alpha *= t

    def _kt_fx_spinin(p, i, t, st, at, s):
        e = _kt_ease_out_cubic(t)
        s.rotate += (1.0 - e) * 360.0
        s.zoom *= max(0.01, e)
        s.alpha *= min(1.0, t * 2.0)

    def _kt_fx_spiral(p, i, t, st, at, s):
        e = _kt_ease_out_cubic(t)
        a = (1.0 - e) * p["turns"] * TAU + i * 0.7
        r = (1.0 - e) * p["radius"]
        s.dx += math.cos(a) * r
        s.dy += math.sin(a) * r
        s.rotate += (1.0 - e) * 180.0
        s.alpha *= t

    def _kt_fx_flip(p, i, t, st, at, s):
        s.xzoom *= max(0.01, abs(math.cos((1.0 - _kt_ease_out_cubic(t)) * math.pi * 0.5)))

    def _kt_fx_impact(p, i, t, st, at, s):
        s.zoom *= 1.0 + (p["scale"] - 1.0) * (1.0 - t) ** 3
        s.alpha *= min(1.0, t * 6.0)
        r = _kt_rng(i, st * 40, 5)
        k = p["shake"] * (1.0 - t)
        s.dx += r.uniform(-k, k)
        s.dy += r.uniform(-k, k)

    def _kt_fx_scramble(p, i, st, at, s):
        st -= i * p.get("stagger", 0.0)
        if st >= p["duration"]:
            return False
        r = _kt_rng(i, at * p["speed"], 6)
        s.char = r.choice(KT_SCRAMBLE_CHARS)
        return True


    ## Exits ------------------------------------------------------------------

    def _kt_fx_shatter(p, i, st, at, s):
        te = st - p["delay"]
        if te <= 0.0:
            return True
        life = 1.4
        if te >= life:
            s.alpha = 0.0
            return False
        r = _kt_rng(i, 8)
        vx = r.uniform(-1.0, 1.0) * p["force"]
        vy = -r.uniform(0.3, 1.0) * p["force"]
        s.dx += vx * te
        s.dy += vy * te + 0.5 * p["gravity"] * te * te
        s.rotate += r.uniform(-1.0, 1.0) * p["spin"] * te
        s.alpha *= max(0.0, 1.0 - te / life)
        return True


    ## Registration -----------------------------------------------------------

    _E = kt_register_effect

    _E("shaky",     _kt_fx_shaky,     [ "speed", "radius", "phase" ], dict(speed=1.5, radius=2.0, phase=2.4))
    _E("irritated", _kt_fx_irritated, [ "intensity", "speed" ], dict(intensity=2.0, speed=30.0))
    _E("tempting",  _kt_fx_tempting,  [ "speed", "phase", "amplitude" ], dict(speed=0.8, phase=0.45, amplitude=4.0))
    _E("sway",      _kt_fx_sway,      [ "speed", "amplitude", "phase" ], dict(speed=0.8, amplitude=3.0, phase=0.4))
    _E("bounce",    _kt_fx_bounce,    [ "speed", "height", "phase" ], dict(speed=1.0, height=6.0, phase=0.35))
    _E("levitate",  _kt_fx_levitate,  [ "speed", "amplitude" ], dict(speed=0.35, amplitude=4.0))
    _E("swing",     _kt_fx_swing,     [ "speed", "angle", "phase" ], dict(speed=1.0, angle=12.0, phase=0.5))
    _E("spin",      _kt_fx_spin,      [ "speed", "phase" ], dict(speed=0.5, phase=0.3))
    _E("drunk",     _kt_fx_drunk,     [ "speed", "sway", "angle", "phase" ], dict(speed=0.5, sway=3.0, angle=6.0, phase=0.6))
    _E("shiver",    _kt_fx_shiver,    [ "intensity", "speed" ], dict(intensity=1.0, speed=45.0))
    _E("pulse",     _kt_fx_pulse,     [ "speed", "amount", "phase" ], dict(speed=1.0, amount=0.15, phase=0.5))
    _E("jelly",     _kt_fx_jelly,     [ "speed", "amount", "phase" ], dict(speed=1.2, amount=0.18, phase=0.5))
    _E("heartbeat", _kt_fx_heartbeat, [ "speed", "amount" ], dict(speed=1.1, amount=0.25))

    _E("flicker",   _kt_fx_flicker,   [ "speed", "min" ], dict(speed=12.0, min=0.25))
    _E("ghost",     _kt_fx_ghost,     [ "speed", "min", "phase" ], dict(speed=0.6, min=0.15, phase=0.4))
    _E("blink",     _kt_fx_blink,     [ "speed", "duty", "phase" ], dict(speed=1.2, duty=0.65, phase=0.0))
    _E("rainbow",   _kt_fx_rainbow,   [ "speed", "spread", "saturation", "value" ], dict(speed=0.4, spread=0.06, saturation=0.6, value=1.0))
    _E("colorwave", _kt_fx_colorwave, [ "colors", "speed", "spread" ], dict(colors="#ff2d75|#ffd23f|#3fd2ff", speed=0.5, spread=0.08))
    _E("glitch",    _kt_fx_glitch,    [ "chance", "speed", "offset" ], dict(chance=0.08, speed=12.0, offset=4.0))

    _E("fadein",  _kt_entrance(_kt_fx_fadein),  [ "duration", "rise", "stagger" ], dict(duration=0.35, rise=10.0, stagger=0.0))
    _E("pop",     _kt_entrance(_kt_fx_pop),     [ "duration", "stagger" ], dict(duration=0.3, stagger=0.0))
    _E("drop",    _kt_entrance(_kt_fx_drop),    [ "duration", "height", "stagger" ], dict(duration=0.5, height=30.0, stagger=0.0))
    _E("slidein", _kt_entrance(_kt_fx_slidein), [ "duration", "distance", "stagger" ], dict(duration=0.35, distance=25.0, stagger=0.0))
    _E("zoomin",  _kt_entrance(_kt_fx_zoomin),  [ "duration", "scale", "stagger" ], dict(duration=0.3, scale=2.5, stagger=0.0))
    _E("spinin",  _kt_entrance(_kt_fx_spinin),  [ "duration", "stagger" ], dict(duration=0.5, stagger=0.0))
    _E("spiral",  _kt_entrance(_kt_fx_spiral),  [ "duration", "radius", "turns", "stagger" ], dict(duration=0.6, radius=40.0, turns=1.0, stagger=0.0))
    _E("flip",    _kt_entrance(_kt_fx_flip),    [ "duration", "stagger" ], dict(duration=0.4, stagger=0.0))
    _E("impact",  _kt_entrance(_kt_fx_impact),  [ "duration", "scale", "shake", "stagger" ], dict(duration=0.45, scale=2.2, shake=4.0, stagger=0.0))
    _E("scramble", _kt_fx_scramble,             [ "duration", "speed", "stagger" ], dict(duration=0.6, speed=20.0, stagger=0.0))

    _E("shatter", _kt_fx_shatter, [ "delay", "force", "gravity", "spin" ], dict(delay=1.2, force=140.0, gravity=500.0, spin=360.0))


    ## {gradient=#c1,#c2,...}  (static, so it works on plain text too) --------

    def _kt_gradient_color(colors, k, n):
        if n <= 1 or len(colors) == 1:
            return colors[0]

        t = float(k) / (n - 1) * (len(colors) - 1)
        seg = min(int(t), len(colors) - 2)

        return Color(colors[seg]).interpolate(Color(colors[seg + 1]), t - seg).hexcode

    def _kt_gradient_tag(tag, value, contents):
        colors = [ c.strip() for c in (value or "").split(",") if c.strip() ]
        if not colors:
            colors = [ "#ff6b6b", "#6bc5ff" ]

        n = 0
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                n += sum(1 for ch in text if not ch.isspace() and ch not in (KT_WJ, KT_ZW))
            elif kind == renpy.TEXT_DISPLAYABLE and isinstance(text, KTLetter):
                n += 1

        rv = [ ]
        k = 0

        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                for ch in text:
                    if ch.isspace() or ch in (KT_WJ, KT_ZW):
                        rv.append((kind, ch))
                    else:
                        rv.append((renpy.TEXT_TAG, "color=" + _kt_gradient_color(colors, k, n)))
                        rv.append((renpy.TEXT_TEXT, ch))
                        rv.append((renpy.TEXT_TAG, "/color"))
                        k += 1

            elif kind == renpy.TEXT_DISPLAYABLE and isinstance(text, KTLetter):
                text.set_color(_kt_gradient_color(colors, k, n))
                rv.append((kind, text))
                k += 1

            else:
                rv.append((kind, text))

        return rv

    config.custom_text_tags["gradient"] = _kt_gradient_tag


    ## Presets ----------------------------------------------------------------

    def kt_preset(name, prefix, suffix=None):
        """
        kt_preset("angry", "{irritated=intensity=3}{color=#ff5544}")

        Creates a {angry}...{/angry} tag. If `suffix` is omitted, closing
        tags are generated from `prefix`.
        """

        if suffix is None:
            opens = _kt_re.findall(r"\{([^/{}][^{}]*)\}", prefix)
            suffix = "".join("{/%s}" % t.partition("=")[0] for t in reversed(opens))

        pre = list(renpy.text.textsupport.tokenize(prefix))
        post = list(renpy.text.textsupport.tokenize(suffix))

        def tag_function(tag, value, contents):
            return pre + list(contents) + post

        config.custom_text_tags[name] = tag_function


    ## Characters -------------------------------------------------------------

    def KTCharacter(name=None, effect=None, cps=None, **kwargs):
        """
        KTCharacter("Ghost", effect="tempting=speed=0.6", cps=25, color="#9fe6ff")

        `effect`  an animated tag (with parameters) applied to every line.
        `cps`     this character's typing speed when typewriter mode is on.
        """

        if cps and kt_typewriter:
            kwargs["what_slow_cps"] = cps

        if effect:
            tag = effect.partition("=")[0]
            kwargs["what_prefix"] = "{%s}" % effect + kwargs.get("what_prefix", "")
            kwargs["what_suffix"] = kwargs.get("what_suffix", "") + "{/%s}" % tag

        return Character(name, **kwargs)


    ## Typing blips:  Character(..., callback=kt_blip("audio/blip.ogg")) ------

    renpy.music.register_channel("kt_blip", mixer="sfx", loop=True)

    def kt_blip(sound):

        def callback(event, interact=True, **kwargs):
            if not interact or not renpy.loadable(sound):
                return

            if event == "show":
                renpy.sound.play(sound, channel="kt_blip", loop=True)
            elif event in ("slow_done", "end"):
                renpy.sound.stop(channel="kt_blip")

        return callback


    ## Camera -----------------------------------------------------------------

    class KTShaker(object):
        """
        ATL function: shake that fades out over `duration` seconds.
        """

        def __init__(self, strength, duration):
            self.strength = strength
            self.duration = duration

        def __call__(self, trans, st, at):
            if st >= self.duration:
                trans.xoffset = 0
                trans.yoffset = 0
                return None

            k = self.strength * (1.0 - st / self.duration)
            trans.xoffset = int(random.uniform(-k, k))
            trans.yoffset = int(random.uniform(-k, k))
            return 0

    class KTTremble(object):
        """
        ATL function: never-ending small shake.
        """

        def __init__(self, strength):
            self.strength = strength

        def __call__(self, trans, st, at):
            trans.xoffset = random.uniform(-self.strength, self.strength)
            trans.yoffset = random.uniform(-self.strength, self.strength) * 0.5
            return 0.03

    def _kt_tick(trans, st, at):
        # Keeps animated shaders (u_time) redrawing every frame.
        return 0

    _kt_camera_fx = [ ]

    def kt_camera(*transforms, **kwargs):
        """
        $ kt_camera(kt_grayscale)            # flashback
        $ kt_camera(kt_crt, kt_vignette)     # several at once
        """
        global _kt_camera_fx
        _kt_camera_fx = list(transforms)
        renpy.show_layer_at(list(_kt_camera_fx), layer=kwargs.get("layer", "master"))

    def kt_camera_reset(layer="master"):
        global _kt_camera_fx
        _kt_camera_fx = [ ]
        renpy.show_layer_at([ ], layer=layer)

    def kt_screen_shake(strength=12, duration=0.5, layer="master"):
        renpy.show_layer_at(_kt_camera_fx + [ kt_shake(strength, duration) ], layer=layer)

    def kt_zoom_punch(amount=0.08, duration=0.35, layer="master"):
        renpy.show_layer_at(_kt_camera_fx + [ kt_punch(amount, duration) ], layer=layer)

    def kt_lightning(shake=True):
        renpy.with_statement(kt_lightning_flash)
        if shake:
            kt_screen_shake(10, 0.45)
        renpy.with_statement(kt_lightning_flash)


    ## Automatic pauses after punctuation ------------------------------------

    _kt_skip_re = _kt_re.compile(r"(\{\{|\{[^{}]*\}|\[\[|\[[^\[\]]*\])")

    def _kt_punct_filter(s):
        d = getattr(store, "kt_punct_pause", 0)

        if not d:
            return s

        parts = _kt_skip_re.split(s)

        # Even indexes are plain text; odd ones are tags / interpolations.
        for j in range(0, len(parts), 2):
            parts[j] = _kt_re.sub(r"([.!?…]+|[,;:])(?=\s)", r"\1{w=%s}" % d, parts[j])

        return "".join(parts)


## Screen shaders (classic GLSL, as used by Ren'Py 8.5). -----------------------

init -5 python:

    renpy.register_shader("kt.vignette", variables="""
        uniform float u_kt_vignette;
        uniform float u_kt_vignette_radius;
        varying vec2 v_tex_coord;
    """, fragment_300="""
        vec2 l__d = (v_tex_coord - vec2(0.5)) * vec2(1.0, 0.8);
        float l__v = smoothstep(u_kt_vignette_radius, u_kt_vignette_radius + 0.45, length(l__d));
        gl_FragColor.rgb *= 1.0 - l__v * u_kt_vignette;
    """)

    renpy.register_shader("kt.crt", variables="""
        uniform float u_kt_strength;
        uniform float u_time;
        uniform vec2 res0;
        varying vec2 v_tex_coord;
    """, fragment_300="""
        float l__line = 0.5 + 0.5 * sin(v_tex_coord.y * res0.y * 3.14159);
        gl_FragColor.rgb *= 1.0 - u_kt_strength * 0.28 * l__line;
        gl_FragColor.rgb *= 1.0 + u_kt_strength * 0.03 * sin(u_time * 50.0);
        float l__roll = fract(v_tex_coord.y * 0.6 - u_time * 0.12);
        gl_FragColor.rgb *= 1.0 + u_kt_strength * 0.08 * smoothstep(0.92, 1.0, l__roll);
    """)

    renpy.register_shader("kt.chroma", variables="""
        uniform sampler2D tex0;
        uniform vec2 res0;
        uniform float u_kt_amount;
        varying vec2 v_tex_coord;
    """, fragment_250="""
        vec2 l__dir = (v_tex_coord - vec2(0.5)) * 2.0 * u_kt_amount / res0;
        vec4 l__c = texture2D(tex0, v_tex_coord);
        float l__r = texture2D(tex0, v_tex_coord + l__dir).r;
        float l__b = texture2D(tex0, v_tex_coord - l__dir).b;
        gl_FragColor = vec4(l__r, l__c.g, l__b, l__c.a);
    """)

    renpy.register_shader("kt.wave", variables="""
        uniform sampler2D tex0;
        uniform vec2 res0;
        uniform float u_time;
        uniform float u_kt_amount;
        uniform float u_kt_freq;
        uniform float u_kt_speed;
        varying vec2 v_tex_coord;
    """, fragment_250="""
        vec2 l__uv = v_tex_coord;
        l__uv.x += sin(v_tex_coord.y * u_kt_freq + u_time * u_kt_speed) * u_kt_amount / res0.x;
        l__uv.y += cos(v_tex_coord.x * u_kt_freq * 0.7 + u_time * u_kt_speed * 0.8) * u_kt_amount * 0.5 / res0.y;
        gl_FragColor = texture2D(tex0, clamp(l__uv, vec2(0.001), vec2(0.999)));
    """)

    renpy.register_shader("kt.pixelate", variables="""
        uniform sampler2D tex0;
        uniform vec2 res0;
        uniform float u_kt_size;
        varying vec2 v_tex_coord;
    """, fragment_250="""
        vec2 l__px = max(u_kt_size, 1.0) / res0;
        vec2 l__uv = (floor(v_tex_coord / l__px) + 0.5) * l__px;
        gl_FragColor = texture2D(tex0, l__uv);
    """)

    renpy.register_shader("kt.bloom", variables="""
        uniform sampler2D tex0;
        uniform vec2 res0;
        uniform float u_kt_amount;
        varying vec2 v_tex_coord;
    """, fragment_250="""
        vec2 l__o = u_kt_amount / res0;
        vec4 l__c = texture2D(tex0, v_tex_coord);
        vec4 l__b = texture2D(tex0, v_tex_coord + vec2(l__o.x, 0.0));
        l__b += texture2D(tex0, v_tex_coord - vec2(l__o.x, 0.0));
        l__b += texture2D(tex0, v_tex_coord + vec2(0.0, l__o.y));
        l__b += texture2D(tex0, v_tex_coord - vec2(0.0, l__o.y));
        l__b += texture2D(tex0, v_tex_coord + l__o);
        l__b += texture2D(tex0, v_tex_coord - l__o);
        l__b *= 1.0 / 6.0;
        gl_FragColor = max(l__c, l__b * 1.12);
    """)

    renpy.register_shader("kt.grain", variables="""
        uniform float u_time;
        uniform float u_kt_grain;
        varying vec2 v_tex_coord;
    """, fragment_320="""
        vec2 l__p = v_tex_coord * 731.0 + vec2(fract(u_time * 7.13) * 91.0, fract(u_time * 3.71) * 57.0);
        float l__n = fract(sin(dot(l__p, vec2(12.9898, 78.233))) * 43758.5453);
        gl_FragColor.rgb += (l__n - 0.5) * u_kt_grain * gl_FragColor.a;
    """)

    renpy.register_shader("kt.screenglitch", variables="""
        uniform sampler2D tex0;
        uniform float u_time;
        uniform float u_kt_amount;
        varying vec2 v_tex_coord;
    """, fragment_250="""
        float l__t = floor(u_time * 14.0);
        float l__band = floor(v_tex_coord.y * 28.0);
        float l__r = fract(sin(l__band * 91.7 + l__t * 37.3) * 43758.5453);
        float l__shift = (l__r > 0.82) ? (l__r - 0.82) * u_kt_amount : 0.0;
        vec2 l__uv = vec2(fract(v_tex_coord.x + l__shift), v_tex_coord.y);
        vec4 l__c = texture2D(tex0, l__uv);
        l__c.r = texture2D(tex0, vec2(fract(l__uv.x + l__shift * 0.6), l__uv.y)).r;
        l__c.b = texture2D(tex0, vec2(fract(l__uv.x - l__shift * 0.6), l__uv.y)).b;
        gl_FragColor = l__c;
    """)


## Text filters, typewriter, click-to-continue. --------------------------------

init 900 python:

    _kt_prev_filter = config.say_menu_text_filter

    def _kt_text_filter(s):
        if _kt_prev_filter is not None:
            s = _kt_prev_filter(s)
        return _kt_punct_filter(s)

    config.say_menu_text_filter = _kt_text_filter


init 999 python:

    # Typewriter mode: clicking during typing completes the line (Ren'Py's
    # built-in behavior for slow text); the next click advances.
    if kt_typewriter:
        style.say_dialogue.slow_cps = kt_typewriter_cps
        style.nvl_dialogue.slow_cps = kt_typewriter_cps



## Placeholders, so the showcase still runs without the PNGs. (Runs after
## Ren'Py has scanned the images folder.)
init 1950 python:

    if not renpy.has_image("bg plaza", exact=True):
        renpy.image("bg plaza", Solid("#3a3550"))


init -1 python:

    if kt_show_ctc:
        adv = Character(kind=adv, ctc="kt_ctc_arrow", ctc_position="nestled")
        _narrator = Character(None, kind=adv, what_style="say_thought")
        adv_narrator = _narrator


################################################################################
## STYLES
################################################################################

## Animated letters look like dialogue text, minus its box layout.
## Change this (or pass style=... to a tag) for text that isn't dialogue.
style kt_letter is say_dialogue:
    xpos 0
    ypos 0
    xanchor 0
    yanchor 0
    xminimum 0
    xmaximum None
    yminimum 0
    ymaximum None


################################################################################
## SPRITE TRANSFORMS
################################################################################

## Place a sprite in the middle of the screen (above the textbox).
transform kt_stage(x=0.5, y=0.45):
    xanchor 0.5 yanchor 0.5 xpos x ypos y

## Gentle up-and-down bob.
transform kt_float(height=12, period=2.6):
    yoffset 0
    block:
        ease (period / 2.0) yoffset -height
        ease (period / 2.0) yoffset 0
        repeat

## Quick hop.
transform kt_hop(height=30):
    easein 0.12 yoffset -height
    easeout 0.15 yoffset 0

## Squash, jump, land, wobble.
transform kt_squash(height=40):
    subpixel True
    ease 0.12 xzoom 1.15 yzoom 0.82
    easein 0.16 xzoom 0.9 yzoom 1.12 yoffset -height
    easeout 0.18 xzoom 1.0 yzoom 1.0 yoffset 0
    ease 0.08 xzoom 1.12 yzoom 0.88
    ease 0.12 xzoom 1.0 yzoom 1.0

## Shake once (fades out).
transform kt_shake(strength=12, duration=0.5):
    function KTShaker(strength, duration)

## Keep trembling until replaced.
transform kt_tremble(strength=2):
    function KTTremble(strength)

## Small nod.
transform kt_nod:
    ease 0.12 yoffset 10
    ease 0.18 yoffset 0

## Idle breathing.
transform kt_breathe(amount=0.012, period=3.0):
    block:
        ease (period / 2.0) yzoom (1.0 + amount)
        ease (period / 2.0) yzoom 1.0
        repeat

## Pulsing glow.
transform kt_glow(amount=0.25, period=1.6):
    block:
        ease (period / 2.0) matrixcolor BrightnessMatrix(amount)
        ease (period / 2.0) matrixcolor BrightnessMatrix(0.0)
        repeat

## See-through and drifting.
transform kt_ghostly:
    alpha 0.0
    linear 0.6 alpha 0.55 matrixcolor TintMatrix("#b8d4ff")
    block:
        ease 2.0 yoffset -10
        ease 2.0 yoffset 0
        repeat

## Black silhouette (mystery character).
transform kt_silhouette:
    linear 0.3 matrixcolor BrightnessMatrix(-1.0)

## Spin and grow into view.
transform kt_spin_in(t=0.6):
    zoom 0.0 rotate -360 alpha 0.0
    easein t zoom 1.0 rotate 0 alpha 1.0

## Dramatic close-up.
transform kt_focus(amount=1.35, t=0.6):
    subpixel True
    easein t zoom amount

## Face the other way.
transform kt_flip(t=0.25):
    ease t xzoom -1.0

## Slide in from off-screen.
transform kt_slide_in_left(x=0.25, t=0.5):
    xalign -0.4 yalign 1.0
    easein t xalign x

transform kt_slide_in_right(x=0.75, t=0.5):
    xalign 1.4 yalign 1.0
    easein t xalign x

## Dim a sprite that isn't speaking (and restore it).
transform kt_dim:
    linear 0.2 matrixcolor BrightnessMatrix(-0.25)

transform kt_undim:
    linear 0.2 matrixcolor BrightnessMatrix(0.0)

## Extra positions.
transform kt_far_left:
    xalign 0.0 yalign 1.0

transform kt_far_right:
    xalign 1.0 yalign 1.0


################################################################################
## COLOR FILTERS / TIME OF DAY  (on a background, or the camera)
################################################################################

transform kt_day:
    linear 1.0 matrixcolor TintMatrix("#fff8ee") * SaturationMatrix(1.05)

transform kt_dawn:
    linear 1.0 matrixcolor TintMatrix("#ffd2e6") * BrightnessMatrix(-0.04) * SaturationMatrix(0.9)

transform kt_evening:
    linear 1.0 matrixcolor TintMatrix("#ffb27a") * SaturationMatrix(1.15)

transform kt_night:
    linear 1.0 matrixcolor TintMatrix("#7a8cff") * BrightnessMatrix(-0.22) * SaturationMatrix(0.55)

transform kt_grayscale:
    linear 0.4 matrixcolor SaturationMatrix(0.0)

transform kt_sepia:
    linear 0.4 matrixcolor SepiaMatrix()

transform kt_invert:
    linear 0.3 matrixcolor InvertMatrix()

transform kt_nightmare:
    linear 0.4 matrixcolor TintMatrix("#ff6060") * SaturationMatrix(0.3)

transform kt_blur(amount=6):
    linear 0.4 blur amount

transform kt_woozy(strength=1.0):
    subpixel True
    xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
    zoom 1.04
    block:
        ease 1.6 rotate (1.2 * strength) xoffset (6 * strength)
        ease 1.6 rotate (-1.2 * strength) xoffset (-6 * strength)
        repeat

transform kt_punch(amount=0.08, duration=0.35):
    subpixel True
    xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
    zoom (1.0 + amount)
    easein duration zoom 1.0


################################################################################
## SHADER CAMERA FILTERS   $ kt_camera(kt_crt)
################################################################################

transform kt_vignette(strength=0.75, radius=0.3):
    mesh True
    shader "kt.vignette"
    u_kt_vignette 0.0 u_kt_vignette_radius radius
    linear 0.5 u_kt_vignette strength

transform kt_crt(strength=1.0):
    mesh True
    shader [ "kt.crt", "kt.vignette" ]
    u_kt_strength strength u_kt_vignette 0.7 u_kt_vignette_radius 0.25
    function _kt_tick

transform kt_chroma(amount=4.0):
    mesh True
    shader "kt.chroma"
    u_kt_amount 0.0
    linear 0.3 u_kt_amount amount

transform kt_haze(amount=4.0, freq=40.0, speed=3.0):
    mesh True
    shader "kt.wave"
    u_kt_amount amount u_kt_freq freq u_kt_speed speed
    function _kt_tick

transform kt_underwater:
    mesh True
    shader "kt.wave"
    u_kt_amount 9.0 u_kt_freq 9.0 u_kt_speed 1.6
    matrixcolor TintMatrix("#7fd4ff") * SaturationMatrix(0.8)
    function _kt_tick

transform kt_pixelate(size=10.0):
    mesh True
    shader "kt.pixelate"
    u_kt_size 1.0
    linear 0.4 u_kt_size size

transform kt_bloom(amount=6.0):
    mesh True
    shader "kt.bloom"
    u_kt_amount amount

transform kt_grain(amount=0.12):
    mesh True
    shader "kt.grain"
    u_kt_grain amount
    function _kt_tick

transform kt_vhs:
    mesh True
    shader [ "kt.chroma", "kt.crt", "kt.vignette", "kt.grain" ]
    u_kt_amount 3.0 u_kt_strength 0.8 u_kt_grain 0.1 u_kt_vignette 0.6 u_kt_vignette_radius 0.3
    function _kt_tick

transform kt_screenglitch(amount=0.6):
    mesh True
    shader "kt.screenglitch"
    u_kt_amount amount
    function _kt_tick


################################################################################
## WEATHER   show kt_rain   /   hide kt_rain
################################################################################

image kt_raindrop = Transform(Solid("#c8dcff70", xysize=(2, 30)), rotate=8)
image kt_snowflake = Transform(Solid("#ffffffdd", xysize=(8, 8)), blur=2.0)
image kt_snowflake_small = Transform(Solid("#ffffffaa", xysize=(4, 4)), blur=1.0)

image kt_petal:
    Solid("#ffc4dcee", xysize=(14, 8))
    rotate 0
    linear 2.2 rotate 360
    repeat

image kt_ember:
    Transform(Solid("#ffb25a", xysize=(5, 5)), blur=1.5)
    alpha 1.0
    linear 0.4 alpha 0.4
    linear 0.4 alpha 1.0
    repeat

image kt_firefly:
    Transform(Solid("#e8ff8c", xysize=(7, 7)), blur=3.0)
    alpha 0.2
    ease 1.2 alpha 1.0
    ease 1.4 alpha 0.15
    repeat

image kt_mote = Transform(Solid("#fff6e0", xysize=(4, 4)), blur=1.5, alpha=0.5)

image kt_rain = SnowBlossom("kt_raindrop", count=220, border=60,
                            xspeed=(-160, -120), yspeed=(1400, 1700), start=0, fast=True)

image kt_storm = Fixed(
    Solid("#0a1020a0"),
    SnowBlossom("kt_raindrop", count=420, border=60,
                xspeed=(-420, -320), yspeed=(1800, 2200), start=0, fast=True),
    )

image kt_snow = Fixed(
    SnowBlossom("kt_snowflake_small", count=120, xspeed=(-30, 30), yspeed=(50, 110), start=0, fast=True),
    SnowBlossom("kt_snowflake", count=60, xspeed=(-50, 50), yspeed=(90, 160), start=0, fast=True),
    )

image kt_petals = SnowBlossom("kt_petal", count=45, xspeed=(60, 160), yspeed=(70, 140), start=0, fast=True)

image kt_embers = SnowBlossom("kt_ember", count=60, xspeed=(-40, 40), yspeed=(-160, -70), start=0, fast=True)

image kt_fireflies = SnowBlossom("kt_firefly", count=26, xspeed=(-25, 25), yspeed=(-28, -8), start=0, fast=True)

image kt_dust = SnowBlossom("kt_mote", count=50, xspeed=(-15, 25), yspeed=(8, 22), start=0, fast=True)


################################################################################
## EXTRAS
################################################################################

## Blinking click-to-continue arrow (see kt_show_ctc at the top).
image kt_ctc_arrow:
    Text("▼", size=16, color="#ffffffcc")
    xoffset 8 yoffset 10
    alpha 1.0
    linear 0.45 alpha 0.15
    linear 0.45 alpha 1.0
    repeat

## Chapter card:  call kt_chapter("Chapter 1", "The Beginning")
style kt_chapter_letter is kt_letter:
    size 72
    color "#ffffff"
    outlines [ (3, "#00000088", 0, 0) ]

style kt_chapter_sub_letter is kt_letter:
    size 30
    color "#d8d0ff"

style kt_chapter_title is text:
    size 72
    xalign 0.5

style kt_chapter_sub is text:
    size 30
    xalign 0.5

screen kt_chapter_card(title, subtitle=""):
    zorder 200

    add Solid("#000000d0")

    vbox:
        align (0.5, 0.45)
        spacing 24

        text "{drop=0.7,40,0.06,style=kt_chapter_letter}[title]{/drop}":
            style "kt_chapter_title"

        if subtitle:
            text "{fadein=0.8,12,0.04,style=kt_chapter_sub_letter}[subtitle]{/fadein}":
                style "kt_chapter_sub"

label kt_chapter(title, subtitle="", hold=2.6):
    window hide
    show screen kt_chapter_card(title, subtitle)
    with Dissolve(0.4)
    # Waits `hold` seconds, or until the player clicks.
    $ renpy.pause(hold)
    hide screen kt_chapter_card
    with Dissolve(0.6)
    return

## Transitions.
define kt_flash = Fade(0.08, 0.0, 0.35, color="#ffffff")
define kt_red_flash = Fade(0.08, 0.0, 0.5, color="#aa0000")
define kt_lightning_flash = Fade(0.04, 0.0, 0.12, color="#e8f0ff")
define kt_blackout = Fade(0.5, 0.5, 0.5)
define kt_pixel = Pixellate(0.8, 6)
define kt_quick = Dissolve(0.15)


################################################################################
## YOUR SETTINGS: colors and presets
################################################################################

init python:

    ## Named color tags: {red}text{/red} etc.
    for _name, _hex in [
        ("red", "#ff5c5c"), ("orange", "#ffa64d"), ("yellow", "#ffe066"),
        ("green", "#6be675"), ("cyan", "#5ce1e6"), ("blue", "#5c9dff"),
        ("purple", "#b48cff"), ("pink", "#ff8fd1"), ("gold", "#ffcf40"),
        ("gray", "#9a9a9a"),
        ]:
        kt_preset(_name, "{color=%s}" % _hex)

    ## Presets: combine effects into one tag. Add your own here.
    kt_preset("angry",   "{irritated=intensity=2.5,speed=35}{color=#ff5544}")
    kt_preset("scared",  "{irritated=intensity=1,speed=20}{size=-4}{color=#c9d6ff}")
    kt_preset("dreamy",  "{tempting=speed=0.5,amplitude=3}{color=#e3c8ff}{i}")
    kt_preset("whisper", "{size=-8}{color=#a0a0a0}{i}")
    kt_preset("shout",   "{size=+12}{b}{irritated=intensity=1.5}")
    kt_preset("hacker",  "{scramble=0.5,25,0.03}{color=#5dff8a}")
    kt_preset("cursed",  "{glitch=0.12}{drunk=0.3,2,4}{color=#c03040}")
    kt_preset("love",    "{heartbeat}{color=#ff7eb6}")
    kt_preset("fire",    "{colorwave=#ff3b1f|#ffa41f|#ffe27a,1.4,0.12}{levitate=0.8,2}")
    kt_preset("ice",     "{colorwave=#9be7ff|#ffffff|#7fb8ff,0.3,0.1}{shiver=0.6}")
    kt_preset("neon",    "{flicker=10,0.6}{color=#ff5ad1}{b}")
    kt_preset("spooky",  "{ghost=0.5,0.3}{drunk=0.25,2,3}{color=#b8ffcf}")
    kt_preset("boss",    "{impact=0.5,3,6}{size=+16}{b}{color=#ff4040}")
    kt_preset("crumble", "{shatter=1.0,60,900,200}")

    ## Typing speed for part of a line (typewriter mode).
    kt_preset("slow",    "{cps=*0.35}")
    kt_preset("quick",   "{cps=*2.5}")




################################################################################
## STORY: ВЕРИТИ
################################################################################

## --- Персонажи ---------------------------------------------------------------

## Имя Верити меняется, если он станет призраком.
define v = Character("[verity_title]", color="#e3c840")
define me = Character("Ты", color="#9ad0ff")
define g = Character("Голубь", color="#a0a0b0")
define crow = Character("Ворона", color="#8a8a9c")
define gk = Character("Голубиный Король", color="#d6d6f0")


## --- Переменные ---------------------------------------------------------------

default verity_trust = 0
default kicked = False
default evil_name = "Безымянный Ужас"
default ending_title = ""

default verity_ghost = False          # стал ли Верити призраком
default verity_title = "Верити"
default pigeon_state = ""             # "enemy", "friend" или "sorry"
default crow_friend = False
default heard_backstory = False
default minion = False
default battle = 0


## --- Спрайты Верити после первой главы ----------------------------------------
## "vv" показывает обычного Верити, а если он призрак — спрайт "verity ghost".

image vv normal = ConditionSwitch("verity_ghost", "verity ghost", "True", "verity normal")
image vv sad = ConditionSwitch("verity_ghost", "verity ghost", "True", "verity sad")
image vv crazy = ConditionSwitch("verity_ghost", "verity ghost", "True", "verity crazy")


## --- Позиции и движения -------------------------------------------------------

## Where Verity stands. Change the numbers to move him.
transform verity_pos:
    xalign 0.5
    yalign 0.6

## Падает сверху и подпрыгивает.
transform kt_drop_in(height=700, t=0.7):
    yoffset -height alpha 0.0
    easein_bounce t yoffset 0 alpha 1.0

## Улетает за горизонт, кувыркаясь.
transform kt_fly_away(t=0.8):
    easein t yoffset -900 xoffset 600 rotate 720 zoom 0.2

## Катится.
transform kt_roll:
    block:
        linear 1.0 rotate 360
        rotate 0
        repeat


## --- Экран концовки -------------------------------------------------------------

style kt_ending_letter is kt_letter:
    size 110
    color "#ffcf40"
    outlines [ (4, "#00000099", 0, 0) ]

style kt_ending_title is text:
    size 110
    xalign 0.5

style kt_ending_sub is text:
    size 30
    xalign 0.5
    color "#d8d0ff"

style kt_ending_hint is text:
    size 24
    xalign 0.5
    color "#9a9aaa"

screen ending_card_screen(title):
    zorder 200

    add Solid("#000000")

    vbox:
        align (0.5, 0.42)
        spacing 30

        text "{drop=0.9,60,0.12,style=kt_ending_letter}КОНЕЦ{/drop}":
            style "kt_ending_title"

        text "«[title]»":
            style "kt_ending_sub"

        null height 40

        text "Доверие Верити: [verity_trust]":
            style "kt_ending_hint"


################################################################################
## ГЛАВА 1: ВСТРЕЧА
################################################################################

label start:

    scene bg verity
    with fade

    "Привет. Это моя первая тестовая визуальная новелла. в общем, тут есть Верити."
    "О боже нет он тебя заметил {irritated}аааа{/irritated}"

    play music "audio/surprising_encounter.wav" fadein 0.5

    show bg empty

    show verity normal at verity_pos, kt_drop_in

    v "{shaky=speed=2}Бугагага{/shaky}"

    v "Я тут"
    v "Бойся меня"

    menu:
        "АААААА (испугаться изо всех сил)":
            $ verity_trust += 1
            me "{shout}АААААААААААААА{/shout}"
            v "..."
            show verity crazy at verity_pos, kt_squash
            $ kt_screen_shake(14, 0.5)
            v "Да! ДА! Вот это я понимаю реакция!"
            v "Сто лет никто так не орал. Можешь ещё раз?"
            me "{whisper}аааа{/whisper}"
            show verity normal at verity_pos
            v "Уже не то. Но я ценю старание."

        "«Ты же размером с апельсин»":
            $ verity_trust -= 1
            show verity sad
            v "..."
            v "Я в перспективе большой."
            v "Это ты просто далеко стоишь."
            me "Я стою прямо рядом с тобой."
            show verity normal
            v "Значит, ты тоже маленький. Мы оба маленькие. Бойся."

        "Погладить его":
            $ verity_trust += 1
            "Ты осторожно гладишь Верити по макушке. Он тёплый, как булочка."
            v "Э."
            v "{irritated=intensity=1.5}ЭЙ.{/irritated}"
            v "Это не входит в план устрашения."
            v "...продолжай, но молча."

        "Пнуть его":
            $ kicked = True
            show verity normal at verity_pos, kt_fly_away
            "Ты пинаешь Верити. Он улетает за горизонт с тихим «ииии»."
            hide verity
            "..."
            "Тишина."
            "Где-то вдалеке каркает ворона. Как-то осуждающе."
            show verity bloodied at verity_pos, kt_drop_in
            v "Я вернулся."
            me "Ты весь в крови!"
            v "Это {red}кетчуп{/red}."
            me "Откуда у тебя кетчуп?"
            v "Я ВСЕГДА ношу с собой кетчуп. Для драматизма."
            v "Бойся меня. Но теперь немного по-другому."
            "Верити деловито вытирает кетчуп об траву."
            show verity normal at verity_pos
            with dissolve

    v "Ладно. Раз уж ты тут, слушай мой гениальный план."
    v "Это моя дорога. Я её ужас. Каждый, кто по ней идёт, должен трепетать."
    me "И многие трепещут?"
    show verity sad
    v "Ты первый за три недели."
    show verity normal
    v "Но мне нужно страшное злодейское имя. «Верити» звучит как название шампуня."

    menu:
        "«Тьма Вечная»":
            $ evil_name = "Тьма Вечная"
            v "Тьма... Вечная..."
            v "Да. Я тёмный. Я вечный. Немного жёлтый, но это детали."

        "«Шарик Судьбы»":
            $ evil_name = "Шарик Судьбы"
            v "Шарик Судьбы."
            v "Звучит, будто я предсказываю будущее. Предсказываю: ты будешь бояться."

        "«Мистер Пупсик»":
            $ evil_name = "Мистер Пупсик"
            $ verity_trust -= 1
            v "Нет."
            me "Мистер Пупсик."
            v "НЕТ."
            show verity sad
            v "...ладно, записываю. Но мне это не нравится."

    show verity crazy at verity_pos, kt_hop
    with hpunch
    v "Отныне зови меня {boss}[evil_name]{/boss}!"
    v "Бугагага!"
    "Эхо разносит его смех по пустой дороге. Звучит как писк резиновой уточки."

    "И тут с неба спускается ОН."
    g "{impact}Курлык.{/impact}"
    show verity sad at verity_pos
    v "О нет."
    v "Только не он."
    me "Это... голубь?"
    v "Это мой заклятый враг. Он думает, что я хлебушек."
    g "Курлык курлык."
    "Голубь клюёт Верити прямо в макушку."

    show verity bloodied at verity_pos
    with hpunch

    if kicked:
        v "АЙ! Вот это уже НЕ кетчуп!"
    else:
        v "АЙ! АЙ! Это не входит в мой план!"

    g "Курлык."
    v "Сделай что-нибудь!!"

    menu:
        "Прогнать голубя (махать руками и кричать)":
            jump pigeon_chase

        "Предложить голубю настоящий хлебушек":
            jump pigeon_bread

        "Ничего не делать и смотреть":
            jump pigeon_watch


label pigeon_chase:
    $ pigeon_state = "enemy"

    "Ты машешь руками как сумасшедший ветряк и орёшь что-то бессвязное."
    g "Курлык?!"
    "Голубь оскорблённо улетает..."
    "...но на ветке у дороги он оборачивается и долго смотрит на вас. Не мигая."
    g "Курлык."
    "Это прозвучало как обещание."
    v "..."
    v "Ты... спас меня?"
    "Верити вытирается листиком. Листик не справляется, но он старается."
    show verity normal at verity_pos
    with dissolve
    v "Злодеев не спасают. Это вообще-то против правил."

    if verity_trust >= 1:
        $ minion = True
        v "Но ладно. Ты принят."
        me "Куда принят?"
        show verity crazy at verity_pos, kt_hop
        with hpunch
        v "В приспешники! Будешь пугать людей вместе со мной."
        v "Первый урок. Повторяй за мной. Бугагага."
        me "Бугагага."
        show verity normal
        v "Неплохо. Немного больше зла в голосе."
    else:
        show verity sad
        if evil_name == "Мистер Пупсик":
            v "Я тебя всё ещё не люблю. Особенно за апельсин и Пупсика."
        else:
            v "Я тебя всё ещё не люблю."
        v "Но можешь пока остаться. Бояться."
        show verity normal

    v "А теперь слушай. Голубь вернётся. Голуби всегда возвращаются."
    v "И я знаю, кто его послал."
    jump act2


label pigeon_bread:
    $ pigeon_state = "friend"

    "Ты достаёшь из кармана кусочек хлеба. Почему он там лежал — неважно."
    g "...курлык."
    "Голубь съедает хлеб. Потом смотрит на Верити. Потом снова на тебя."
    "Потом осторожно вытирает Верити крылом. Почти нежно."

    show verity normal at verity_pos
    with dissolve

    v "Он... он больше не хочет меня есть?"
    g "Курлык."
    v "Он говорит, что мы теперь банда."
    me "Ты понимаешь по-голубиному?"
    v "Я понимаю ВСЁ, что касается зла."
    "Верити забирается голубю на спину. Голубь, кажется, не против."
    show verity crazy at verity_pos, kt_fly_away
    v "Отныне я — ЛЕТАЮЩИЙ ужас! Бугагагааааа..."
    hide verity
    "Они улетают. Голос Верити становится всё тише, пока не превращается в маленькое «гага» где-то в облаках."
    "..."
    "Через пять минут они возвращаются."
    show verity normal at verity_pos, kt_drop_in
    v "Голубь устал."
    g "курлык"
    v "Мы решили, что летающий ужас — это проект на будущее."
    v "Зато голубь мне кое-что рассказал. Кое-что важное."
    jump act2


label pigeon_watch:
    "Ты стоишь и смотришь."
    "Голубь клюёт. Верити пищит."
    "Голубь клюёт ещё. Верити пищит тише."
    v "Ты... серьёзно... просто смотришь..."
    g "Курлык."

    stop music fadeout 3.0

    v "Запомни меня..."
    v "...страшным..."

    show verity dead at verity_pos
    with dissolve

    "Верити больше не двигается."
    "Голубь задумчиво смотрит на него. Потом на тебя."
    g "...курлык."
    "Голубь улетает, так ничего и не съев. Видимо, из уважения."
    "Ты кладёшь на дорогу маленький камешек."
    "На нём нацарапано: «[evil_name]. Бойтесь его.»"
    "Где-то вдалеке опять каркает ворона. Всё так же осуждающе."

    show kt_rain
    "Начинается дождь. Конечно, начинается дождь."
    "..."
    "..."

    $ pigeon_state = "sorry"
    $ verity_ghost = True
    $ verity_title = "Призрак Верити"

    show verity ghost at verity_pos
    with dissolve

    "Над камешком медленно поднимается что-то полупрозрачное."
    v "..."
    v "Почему я выгляжу как этот чёртов призрак из Пакмана?"
    v "Ой, да какая разница."
    v "Серьёзно."
    v "{irritated=intensity=2}{size=+20}Какая{/size}{/irritated}"
    $ kt_screen_shake(10, 0.4)
    v "{irritated=intensity=5,speed=45}{size=+30}разница.{/size}{/irritated}"

    hide kt_rain
    "Дождь стихает."
    me "Ты... призрак?"
    v "Я — призрак ужаса. Звучит намного лучше, чем шампунь."
    v "Минусы: я ничего не могу трогать. Даже кетчуп."
    v "Плюсы: голубь меня больше не клюнет. Клюв пройдёт насквозь."
    v "И теперь у меня есть время. Целая вечность. Для мести."
    v "И ты мне поможешь. Потому что ты смотрел."
    me "...справедливо."

    play music "audio/surprising_encounter.wav" fadein 2.0
    jump act2


################################################################################
## ГЛАВА 2: ДОРОГА
################################################################################

label act2:

    call kt_chapter("Глава 2", "Дорога") from _call_kt_chapter

    scene bg empty at kt_evening
    with dissolve
    show vv normal at verity_pos
    with dissolve

    v "Итак. Голубь прилетел не сам."
    v "Его послал {boss}Голубиный Король{/boss}."
    me "Голубиный... кто?"
    v "Король. Всех голубей этой округи. Он живёт в конце дороги, на Старой площади у озера."
    v "Он давно хочет мою дорогу. Здесь прохожие роняют больше всего крошек."
    v "Если я напугаю его прямо у него дома, на глазах у всей стаи..."
    v "...дорога станет моей. Навсегда. И меня наконец начнут бояться."

    if verity_ghost:
        v "А ещё он должен ответить за то, что со мной сделал. Я буду его преследовать. Это то, что делают призраки."

    v "Путь неблизкий. Как ты меня понесёшь?"

    menu:
        "Посадить Верити на плечо":
            $ verity_trust += 1
            if verity_ghost:
                "Ты протягиваешь руки, но они проходят сквозь него. Верити всё равно устраивается у тебя на плече."
                "От него немножко холодно. Как от открытого холодильника."
            else:
                "Ты сажаешь Верити на плечо. Он сидит там с видом великого полководца."
            v "Вперёд, мой скакун! ...то есть приспешник."

        "Пусть катится сам":
            if verity_ghost:
                "Верити пытается катиться, но призраки не катятся. Он просто плывёт рядом, обиженно."
                v "Я плыву. Это унизительно."
            else:
                show vv normal at verity_pos, kt_roll
                "Верити катится рядом с тобой по асфальту. Подпрыгивает на каждом камешке."
                v "Я качусь. Это унизительно, но эффективно."
                show vv normal at verity_pos

    ## --- Ворона ---

    "Через час дорогу вам преграждает..."
    "...ворона."
    crow "Кар."
    show vv sad
    v "О нет. Это ОНА."
    me "Ты её знаешь?"
    v "Это та самая ворона. Она осуждает всё, что видит."
    v "Она осуждала, как я пищал. Она осуждала облака. Однажды она осуждала солнце. Солнце зашло."
    crow "Кар."
    v "Она говорит, что пропустит нас, только если ты ответишь на загадку."
    crow "Кар кар. Кар-кар. Кар?"
    v "«Что маленькое, жёлтое и наводит ужас на всю округу?»"

    menu:
        "«Верити»":
            $ crow_friend = True
            $ verity_trust += 1
            crow "..."
            crow "Кар."
            v "Она... она кивнула."
            v "Она НЕ осудила."
            show vv crazy at verity_pos, kt_hop
            v "Впервые в истории!"
            "Ворона отходит в сторону. В её взгляде впервые что-то похожее на уважение."

        "«Лимон»":
            crow "Кар."
            "Ворона смотрит на тебя осуждающе. Потом на Верити. Ещё более осуждающе."
            v "Лимон. Я — лимон. Спасибо."
            "Но ворона всё же отходит в сторону. Видимо, ей просто стало вас жаль."

        "«Цыплёнок»":
            crow "КАР."
            v "Она говорит, что цыплята — это вообще-то очень страшно. Ты их просто не видел ночью."
            "Ворона отходит, явно разочарованная в вас обоих."

    ## --- Ночь ---

    scene bg empty at kt_night
    with kt_blackout
    show kt_fireflies
    show vv normal at verity_pos
    with dissolve

    "Темнеет. Над дорогой зажигаются светлячки."
    v "До площади не успеем. Привал."
    "Вы садитесь у обочины. Верити долго молчит, что на него совсем не похоже."
    me "Верити... а как ты вообще стал ужасом?"
    show vv sad
    v "..."
    v "Ладно. Только никому."

    hide kt_fireflies
    $ kt_camera(kt_sepia)
    $ heard_backstory = True

    v "Я родился в автомате с жвачкой. У ларька на углу."
    v "Все шарики там были красные, зелёные, синие. А я — жёлтый."
    v "Каждый день кто-то бросал монетку. И каждый день выкатывался кто-то другой."
    v "Три года. {slow}Три года я смотрел через стекло.{/slow}"
    v "А потом автомат сломался, и я выкатился на дорогу."
    v "И я подумал: раз меня никто не выбрал..."
    v "...пусть меня хотя бы боятся."

    $ kt_camera_reset()
    show kt_fireflies

    if verity_ghost:
        v "А теперь у меня даже тела нет. Даже жёлтого."

    menu:
        "«Я бы тебя выбрал»":
            $ verity_trust += 2
            v "..."
            v "Ты это просто так говоришь."
            me "Нет. Я бы бросил монетку только ради тебя."
            v "...бойся меня, пожалуйста, прямо сейчас, потому что у меня что-то попало в глаз."

        "«Так ты буквально жвачка?»":
            $ verity_trust -= 1
            v "Я НЕ ЖВАЧКА."
            v "Я шарик. Это разное. Жвачку жуют. Меня — боятся."
            v "...никому не говори."

        "Молча сесть поближе":
            $ verity_trust += 1
            "Ты молча придвигаешься ближе. Верити ничего не говорит, но и не отодвигается."
            v "...спасибо."

    show vv normal
    "Вы засыпаете под светлячками."

    ## --- Утро ---

    scene bg empty at kt_dawn
    with kt_blackout
    show vv normal at verity_pos
    with dissolve

    "Утро."

    if pigeon_state == "enemy":
        "На проводах над дорогой сидят голуби. Много голубей."
        "Они все смотрят на вас."
        g "курлык"
        show vv sad
        v "Это разведка. Король знает, что мы идём."
        show vv normal

    elif pigeon_state == "friend":
        "С неба спускается знакомый голубь и садится тебе на плечо."
        g "Курлык!"
        v "Он говорит, что Король узнал про нас. И очень зол."
        v "И что он, наш голубь, теперь предатель короны. Ради нас."
        g "Курлык."
        v "Не надо сантиментов. Мы злодеи."
        v "...но спасибо."

    else:
        "Посреди дороги лежит кусочек хлеба. А за ним, у кустов, прячется голубь."
        "Тот самый."
        g "...курлык."
        v "ТЫ."
        g "Курлык курлык."
        v "Он говорит, что не хотел... ну. Совсем."
        v "Его послал Король. А он не знал, что я такой хрупкий."
        v "Теперь он хочет помочь. Искупить вину."
        v "Ладно. Но хлеб я забираю."
        me "Ты не можешь его взять. Ты призрак."
        show vv sad
        v "...тогда ты забери. Для меня."
        "Ты кладёшь хлеб в карман. Голубь виновато шагает за вами."
        show vv normal

    ## --- Дождь ---

    show kt_rain
    "Начинается дождь."

    if verity_ghost:
        v "Ха. Дождь проходит сквозь меня. Даже обидно — не на что жаловаться."
    else:
        show vv sad
        v "Нет-нет-нет. Вода. Я из сахара. Наверное. Я никогда не проверял!"

        menu:
            "Укрыть его ладонями":
                $ verity_trust += 1
                "Ты накрываешь Верити ладонями. Под ними сухо и тепло."
                v "...это чисто тактическое укрытие."

            "«Сейчас и проверим»":
                $ verity_trust -= 1
                "Ты ждёшь. Верити мокнет. Верити не растворяется."
                v "Ну вот. Теперь я не знаю, из чего я сделан. Спасибо."
                v "У меня экзистенциальный кризис."

        show vv normal

    hide kt_rain
    "Дождь заканчивается. Далеко впереди, над озером, из тумана поднимаются колонны."
    v "Пришли."

    jump act3


################################################################################
## ГЛАВА 3: ГОЛУБИНЫЙ КОРОЛЬ
################################################################################

label act3:

    call kt_chapter("Глава 3", "Голубиный Король") from _call_kt_chapter_1

    $ battle = 0

    scene bg plaza
    with dissolve

    "Старая площадь. Колонны, вода и закатное небо."
    "На каждом карнизе, на каждой колонне сидят голуби. Сотни голубей."

    show vv normal at verity_pos
    with dissolve

    if evil_name == "Шарик Судьбы":
        "В центре площади на постаменте стоит большой светящийся шар. Старый фонарь."
        v "Подожди. У них тут свой шар? Большой? Светится?"
        v "Он украл мой образ."

    v "Вот она. Голубиная столица."
    v "Подходим. Медленно. Злодейски."
    "Двое голубей-стражников преграждают вам путь."
    g "Курлык."
    v "Они говорят, что к Королю нельзя. И что я похож на хлебушек."
    show vv sad
    v "ПОЧЕМУ ВСЕ ЭТО ГОВОРЯТ."
    v "Помоги мне! Как пройти?"

    menu:
        "Научить его по-настоящему страшному смеху":
            $ battle += 1
            me "Смотри. Ниже. Громче. С душой."
            me "{shout}БУ-ГА-ГА-ГА.{/shout}"
            $ kt_screen_shake(10, 0.4)
            "Стражники подпрыгивают и улетают на соседнюю колонну."
            show vv crazy
            v "Это мой приспешник! Значит, засчитывается мне!"

        "«Кетчуп!»" if kicked and not verity_ghost:
            $ battle += 1
            me "Верити. Кетчуп. Для драматизма."
            hide vv
            show verity bloodied at verity_pos
            with kt_red_flash
            v "Я ИСТЕКАЮ ЗЛОМ!"
            "Стражники в ужасе разлетаются."
            v "Это кетчуп."
            "Но стражников уже нет."
            hide verity
            show vv normal at verity_pos

        "«Бу!» (если ты призрак, это работает лучше)" if verity_ghost:
            $ battle += 1
            v "Бу."
            "Стражники смотрят на призрака. Потом друг на друга. Потом улетают так быстро, что теряют пару перьев."
            v "Вот. Вот ради этого стоило умереть."

        "Пусть пробует сам":
            v "Хорошо."
            v "Бойся меня... пожалуйста..."
            "Стражники переглядываются. Им, кажется, стало неловко, и они просто отходят в сторону."
            show vv sad
            v "Злодеи не бывают милыми."
            show vv normal

    ## --- Голубиный Король ---

    show kt_storm
    $ kt_lightning()

    "Небо темнеет. По площади проходит тень от тысячи крыльев."
    "На вершину колонны опускается голубь. Огромный. В короне из крышечки от бутылки."
    gk "{impact}КУРЛЫК.{/impact}"
    $ kt_screen_shake(16, 0.6)
    show vv sad
    v "Голубиный. Король."

    if pigeon_state == "enemy":
        v "И рядом с ним — тот самый голубь. Он теперь генерал."

    gk "Курлык курлык. КУРЛЫК."
    v "Он говорит, что моя дорога теперь его. И все крошки на ней — тоже."
    v "А нас он... склюёт."

    if crow_friend:
        $ battle += 1
        crow "КАР."
        "Из-за колонны вылетает ворона. Она смотрит на Короля. Осуждающе."
        "Очень осуждающе."
        "Король на мгновение теряется. Никто ещё никогда не осуждал его так сильно."

    if pigeon_state == "friend":
        $ battle += 1
        g "Курлык!"
        "Ваш голубь встаёт между вами и Королём, распушив перья."
        v "Это наш голубь! Наш! Злодейский!"

    elif pigeon_state == "sorry":
        $ battle += 1
        g "курлык..."
        "Тот самый голубь заслоняет Верити крылом. Крыло проходит насквозь, но жест засчитан."

    gk "КУРЛЫК-ВОЛНА!"
    with kt_flash
    $ kt_screen_shake(18, 0.7)
    "На вас летит волна перьев, пыли и голубиного презрения."

    menu:
        "Закрыть Верити собой":
            $ verity_trust += 1
            $ battle += 1
            "Ты прыгаешь вперёд. Волна перьев бьёт тебе в спину. Немного щекотно, немного больно, очень пыльно."
            v "Ты... ты закрыл меня?"

        "Бросить хлеб в сторону":
            $ battle += 1
            "Ты швыряешь хлеб далеко в сторону. Почему в твоих карманах столько хлеба — неважно."
            "Половина голубиной армии с воплями «КУРЛЫК» бросается за ним."
            gk "КУРЛЫК!!"
            v "Он говорит, что у него отвратительная армия."

        "Убежать за колонну":
            $ verity_trust -= 1
            "Ты бежишь за колонну. Верити — нет."
            v "ПРЕДАТЕЛЬ!"
            v "...ладно, вернись. Мне страшно."

    show vv sad
    v "Он... он слишком сильный."
    v "Может, я и правда просто шарик, которого никто не выбрал."

    menu:
        "«Ты самый страшный злодей, которого я знаю!»":
            show vv normal
            v "Правда?"

            menu:
                "«Да.»":
                    me "Да."
                    v "Ты сказал это так, будто читаешь список покупок."
                    me "Да. Молоко. Хлеб. Ты — самый страшный злодей. Яйца."
                    v "..."
                    v "Ладно. Это было убедительно. Особенно яйца."
                    if verity_trust >= 3:
                        $ battle += 2
                    else:
                        $ battle += 1

                "«Нет.»":
                    me "Нет."
                    v "..."
                    show vv crazy
                    v "ЧТО."
                    me "Шучу. Конечно, да."
                    v "НЕ ШУТИ ТАК В РАЗГАР БИТВЫ!!"
                    v "...но это сработало. Я зол. Я ОЧЕНЬ зол."
                    $ battle += 2

        "«Ты не один. Я с тобой.»":
            $ verity_trust += 1
            $ battle += 2
            show vv normal
            v "...со мной."

        "Промолчать":
            v "..."
            v "Понятно."

    if battle >= 3:
        jump boss_win
    else:
        jump ending_pigeon_wins


label boss_win:

    show vv crazy at verity_pos, kt_squash
    v "Хорошо."
    v "Тогда смотри, Голубиный Король."
    v "Смотри, что бывает, когда ужас не один."

    $ kt_camera(kt_nightmare)
    show vv crazy at verity_pos, kt_focus(1.5)

    v "{boss}{shaky=speed=4,radius=4}БУГАГАГАГАГАГА!{/shaky}{/boss}"
    $ kt_screen_shake(22, 1.0)
    $ kt_lightning()

    "Над площадью прокатывается смех. Настоящий. Злодейский. Колонны дрожат. Озеро идёт рябью."

    if minion:
        me "БУГАГАГАГА!"
        "Ты смеёшься вместе с ним. Как он учил. С душой."

    gk "...курлык?"
    "Голубиный Король впервые в жизни пугается."
    "Он падает с колонны прямо на камни. Корона катится к ногам Верити."

    hide kt_storm
    $ kt_camera_reset()
    scene bg plaza at kt_evening
    with kt_blackout
    show vv normal at verity_pos
    with dissolve

    "Буря уходит. Армия голубей разлетелась. На камнях сидит Король — без короны, взъерошенный и очень маленький."
    gk "...курлык."
    v "Он говорит, что сдаётся. Дорога моя."
    show vv crazy at verity_pos, kt_hop
    v "МОЯ!"
    show vv normal at verity_pos
    v "Ну что, приспешник. Что с ним делать?"

    menu:
        "Предложить Королю хлеб":
            jump ending_bread_peace

        "Пусть решает Верити":
            jump ending_verity_decides


################################################################################
## КОНЦОВКИ
################################################################################

label ending_bread_peace:
    "Ты достаёшь из кармана последний кусочек хлеба и кладёшь его перед Королём."
    v "Ты... ты кормишь моего врага?"
    gk "...курлык?"
    "Король долго смотрит на хлеб. Потом на тебя. Потом на Верити."
    "Потом съедает хлеб и низко кланяется."
    v "Он говорит... спасибо."
    v "И что я теперь почётный член стаи. Меня больше никогда не клюнут."
    v "Я всё ещё злодей. Просто теперь у меня есть армия голубей."

    if pigeon_state == "friend" and not verity_ghost:
        "Верити забирается на спину своему голубю."
        show vv crazy at verity_pos, kt_fly_away
        v "Бугагагааааа..."
        "Теперь у летающего ужаса есть целая эскадрилья."
        $ ending_title = "Воздушный Ужас"
    else:
        $ ending_title = "Хлебный Мир"
    jump ending_card


label ending_verity_decides:
    v "Я?"
    v "..."

    if verity_trust >= 5:
        jump ending_true

    v "Кыш."
    gk "Курлык!"
    "Король улетает, теряя перья. Верити смотрит ему вслед с огромным удовлетворением."

    if verity_ghost:
        v "Я буду являться ему каждую ночь. До конца его голубиных дней."
        v "А ты... можешь заходить. Иногда. Призракам тоже бывает скучно."
        $ ending_title = "Призрак Дороги"
    else:
        show vv sad
        v "Я тебя всё ещё не очень люблю."
        v "Но можешь иногда приходить. Бояться."
        $ ending_title = "Неохотная дружба"
    jump ending_card


label ending_true:
    v "Знаешь..."
    v "Я ведь хотел, чтобы меня боялись. Потому что думал, что меня никто никогда не выберет."
    v "А потом на мою дорогу пришёл ты."
    v "И ты... ну."
    v "{slow}Ты меня выбрал.{/slow}"
    me "Конечно выбрал."
    v "..."
    v "Отпусти его. Мне больше не нужна его дорога."
    v "Мне хватит нашей."
    "Король улетает. Над озером садится солнце."
    show vv crazy at verity_pos, kt_hop
    v "Ну что, приспешник?"
    v "Пойдём пугать мир?"
    me "Пойдём."
    v "{shaky}Бугагага!{/shaky}"
    me "{shaky}Бугагага!{/shaky}"

    if crow_friend:
        "Где-то на колонне ворона смотрит на вас. И впервые за всю историю мира — одобрительно."

    $ ending_title = "Ужас Дороги и его Приспешник"
    jump ending_card


label ending_pigeon_wins:
    gk "КУРЛЫК."
    $ kt_screen_shake(18, 0.8)
    "Голубиный Король взмахивает крыльями, и вас просто выдувает с площади."
    "Вы приземляетесь в кусты на краю дороги."
    show vv sad at verity_pos
    v "Мы проиграли..."
    v "Дорога теперь его. И все крошки на ней."
    v "Запомни меня страшным, ладно?"
    "Голубиная армия улетает праздновать. Становится очень тихо."
    "Где-то на колонне ворона смотрит вслед Королю. Осуждающе."
    "Хоть кто-то на вашей стороне."
    $ ending_title = "Голубь Победил"
    jump ending_card


label ending_card:
    stop music fadeout 1.0
    $ kt_camera_reset()
    scene black
    with fade
    window hide
    show screen ending_card_screen(ending_title)
    with Dissolve(1.0)
    $ renpy.pause()
    hide screen ending_card_screen
    with Dissolve(1.0)
    return
