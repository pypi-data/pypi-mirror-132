from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Mesh3d(_BaseTraceType):

    # class properties
    # --------------------
    _parent_path_str = ""
    _path_str = "mesh3d"
    _valid_props = {
        "alphahull",
        "autocolorscale",
        "cauto",
        "cmax",
        "cmid",
        "cmin",
        "color",
        "coloraxis",
        "colorbar",
        "colorscale",
        "contour",
        "customdata",
        "customdatasrc",
        "delaunayaxis",
        "facecolor",
        "facecolorsrc",
        "flatshading",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hovertemplate",
        "hovertemplatesrc",
        "hovertext",
        "hovertextsrc",
        "i",
        "ids",
        "idssrc",
        "intensity",
        "intensitymode",
        "intensitysrc",
        "isrc",
        "j",
        "jsrc",
        "k",
        "ksrc",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "lighting",
        "lightposition",
        "meta",
        "metasrc",
        "name",
        "opacity",
        "reversescale",
        "scene",
        "showlegend",
        "showscale",
        "stream",
        "text",
        "textsrc",
        "type",
        "uid",
        "uirevision",
        "vertexcolor",
        "vertexcolorsrc",
        "visible",
        "x",
        "xcalendar",
        "xhoverformat",
        "xsrc",
        "y",
        "ycalendar",
        "yhoverformat",
        "ysrc",
        "z",
        "zcalendar",
        "zhoverformat",
        "zsrc",
    }

    # alphahull
    # ---------
    @property
    def alphahull(self):
        """
        Determines how the mesh surface triangles are derived from the
        set of vertices (points) represented by the `x`, `y` and `z`
        arrays, if the `i`, `j`, `k` arrays are not supplied. For
        general use of `mesh3d` it is preferred that `i`, `j`, `k` are
        supplied. If "-1", Delaunay triangulation is used, which is
        mainly suitable if the mesh is a single, more or less layer
        surface that is perpendicular to `delaunayaxis`. In case the
        `delaunayaxis` intersects the mesh surface at more than one
        point it will result triangles that are very long in the
        dimension of `delaunayaxis`. If ">0", the alpha-shape algorithm
        is used. In this case, the positive `alphahull` value signals
        the use of the alpha-shape algorithm, _and_ its value acts as
        the parameter for the mesh fitting. If 0,  the convex-hull
        algorithm is used. It is suitable for convex bodies or if the
        intention is to enclose the `x`, `y` and `z` point set into a
        convex hull.
    
        The 'alphahull' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["alphahull"]

    @alphahull.setter
    def alphahull(self, val):
        self["alphahull"] = val

    # autocolorscale
    # --------------
    @property
    def autocolorscale(self):
        """
        Determines whether the colorscale is a default palette
        (`autocolorscale: true`) or the palette determined by
        `colorscale`. In case `colorscale` is unspecified or
        `autocolorscale` is true, the default  palette will be chosen
        according to whether numbers in the `color` array are all
        positive, all negative or mixed.
    
        The 'autocolorscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["autocolorscale"]

    @autocolorscale.setter
    def autocolorscale(self, val):
        self["autocolorscale"] = val

    # cauto
    # -----
    @property
    def cauto(self):
        """
        Determines whether or not the color domain is computed with
        respect to the input data (here `intensity`) or the bounds set
        in `cmin` and `cmax`  Defaults to `false` when `cmin` and
        `cmax` are set by the user.
    
        The 'cauto' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["cauto"]

    @cauto.setter
    def cauto(self, val):
        self["cauto"] = val

    # cmax
    # ----
    @property
    def cmax(self):
        """
        Sets the upper bound of the color domain. Value should have the
        same units as `intensity` and if set, `cmin` must be set as
        well.
    
        The 'cmax' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmax"]

    @cmax.setter
    def cmax(self, val):
        self["cmax"] = val

    # cmid
    # ----
    @property
    def cmid(self):
        """
        Sets the mid-point of the color domain by scaling `cmin` and/or
        `cmax` to be equidistant to this point. Value should have the
        same units as `intensity`. Has no effect when `cauto` is
        `false`.
    
        The 'cmid' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmid"]

    @cmid.setter
    def cmid(self, val):
        self["cmid"] = val

    # cmin
    # ----
    @property
    def cmin(self):
        """
        Sets the lower bound of the color domain. Value should have the
        same units as `intensity` and if set, `cmax` must be set as
        well.
    
        The 'cmin' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["cmin"]

    @cmin.setter
    def cmin(self, val):
        self["cmin"] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets the color of the whole mesh
    
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen
          - A number that will be interpreted as a color
            according to mesh3d.colorscale

        Returns
        -------
        str
        """
        return self["color"]

    @color.setter
    def color(self, val):
        self["color"] = val

    # coloraxis
    # ---------
    @property
    def coloraxis(self):
        """
        Sets a reference to a shared color axis. References to these
        shared color axes are "coloraxis", "coloraxis2", "coloraxis3",
        etc. Settings for these shared color axes are set in the
        layout, under `layout.coloraxis`, `layout.coloraxis2`, etc.
        Note that multiple color scales can be linked to the same color
        axis.
    
        The 'coloraxis' property is an identifier of a particular
        subplot, of type 'coloraxis', that may be specified as the string 'coloraxis'
        optionally followed by an integer >= 1
        (e.g. 'coloraxis', 'coloraxis1', 'coloraxis2', 'coloraxis3', etc.)

        Returns
        -------
        str
        """
        return self["coloraxis"]

    @coloraxis.setter
    def coloraxis(self, val):
        self["coloraxis"] = val

    # colorbar
    # --------
    @property
    def colorbar(self):
        """
        The 'colorbar' property is an instance of ColorBar
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.mesh3d.ColorBar`
          - A dict of string/value properties that will be passed
            to the ColorBar constructor
    
            Supported dict properties:
                
                bgcolor
                    Sets the color of padded area.
                bordercolor
                    Sets the axis line color.
                borderwidth
                    Sets the width (in px) or the border enclosing
                    this color bar.
                dtick
                    Sets the step in-between ticks on this axis.
                    Use with `tick0`. Must be a positive number, or
                    special strings available to "log" and "date"
                    axes. If the axis `type` is "log", then ticks
                    are set every 10^(n*dtick) where n is the tick
                    number. For example, to set a tick mark at 1,
                    10, 100, 1000, ... set dtick to 1. To set tick
                    marks at 1, 100, 10000, ... set dtick to 2. To
                    set tick marks at 1, 5, 25, 125, 625, 3125, ...
                    set dtick to log_10(5), or 0.69897000433. "log"
                    has several special values; "L<f>", where `f`
                    is a positive number, gives ticks linearly
                    spaced in value (but not position). For example
                    `tick0` = 0.1, `dtick` = "L0.5" will put ticks
                    at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10
                    plus small digits between, use "D1" (all
                    digits) or "D2" (only 2 and 5). `tick0` is
                    ignored for "D1" and "D2". If the axis `type`
                    is "date", then you must convert the time to
                    milliseconds. For example, to set the interval
                    between ticks to one day, set `dtick` to
                    86400000.0. "date" also has special values
                    "M<n>" gives ticks spaced by a number of
                    months. `n` must be a positive integer. To set
                    ticks on the 15th of every third month, set
                    `tick0` to "2000-01-15" and `dtick` to "M3". To
                    set ticks every 4 years, set `dtick` to "M48"
                exponentformat
                    Determines a formatting rule for the tick
                    exponents. For example, consider the number
                    1,000,000,000. If "none", it appears as
                    1,000,000,000. If "e", 1e+9. If "E", 1E+9. If
                    "power", 1x10^9 (with 9 in a super script). If
                    "SI", 1G. If "B", 1B.
                len
                    Sets the length of the color bar This measure
                    excludes the padding of both ends. That is, the
                    color bar length is this length minus the
                    padding on both ends.
                lenmode
                    Determines whether this color bar's length
                    (i.e. the measure in the color variation
                    direction) is set in units of plot "fraction"
                    or in *pixels. Use `len` to set the value.
                minexponent
                    Hide SI prefix for 10^n if |n| is below this
                    number. This only has an effect when
                    `tickformat` is "SI" or "B".
                nticks
                    Specifies the maximum number of ticks for the
                    particular axis. The actual number of ticks
                    will be chosen automatically to be less than or
                    equal to `nticks`. Has an effect only if
                    `tickmode` is set to "auto".
                orientation
                    Sets the orientation of the colorbar.
                outlinecolor
                    Sets the axis line color.
                outlinewidth
                    Sets the width (in px) of the axis line.
                separatethousands
                    If "true", even 4-digit integers are separated
                showexponent
                    If "all", all exponents are shown besides their
                    significands. If "first", only the exponent of
                    the first tick is shown. If "last", only the
                    exponent of the last tick is shown. If "none",
                    no exponents appear.
                showticklabels
                    Determines whether or not the tick labels are
                    drawn.
                showtickprefix
                    If "all", all tick labels are displayed with a
                    prefix. If "first", only the first tick is
                    displayed with a prefix. If "last", only the
                    last tick is displayed with a suffix. If
                    "none", tick prefixes are hidden.
                showticksuffix
                    Same as `showtickprefix` but for tick suffixes.
                thickness
                    Sets the thickness of the color bar This
                    measure excludes the size of the padding, ticks
                    and labels.
                thicknessmode
                    Determines whether this color bar's thickness
                    (i.e. the measure in the constant color
                    direction) is set in units of plot "fraction"
                    or in "pixels". Use `thickness` to set the
                    value.
                tick0
                    Sets the placement of the first tick on this
                    axis. Use with `dtick`. If the axis `type` is
                    "log", then you must take the log of your
                    starting tick (e.g. to set the starting tick to
                    100, set the `tick0` to 2) except when
                    `dtick`=*L<f>* (see `dtick` for more info). If
                    the axis `type` is "date", it should be a date
                    string, like date data. If the axis `type` is
                    "category", it should be a number, using the
                    scale where each category is assigned a serial
                    number from zero in the order it appears.
                tickangle
                    Sets the angle of the tick labels with respect
                    to the horizontal. For example, a `tickangle`
                    of -90 draws the tick labels vertically.
                tickcolor
                    Sets the tick color.
                tickfont
                    Sets the color bar's tick label font
                tickformat
                    Sets the tick label formatting rule using d3
                    formatting mini-languages which are very
                    similar to those in Python. For numbers, see: h
                    ttps://github.com/d3/d3-format/tree/v1.4.5#d3-f
                    ormat. And for dates see:
                    https://github.com/d3/d3-time-
                    format/tree/v2.2.3#locale_format. We add two
                    items to d3's date formatter: "%h" for half of
                    the year as a decimal number as well as "%{n}f"
                    for fractional seconds with n digits. For
                    example, *2016-10-13 09:15:23.456* with
                    tickformat "%H~%M~%S.%2f" would display
                    "09~15~23.46"
                tickformatstops
                    A tuple of :class:`plotly.graph_objects.mesh3d.
                    colorbar.Tickformatstop` instances or dicts
                    with compatible properties
                tickformatstopdefaults
                    When used in a template (as layout.template.dat
                    a.mesh3d.colorbar.tickformatstopdefaults), sets
                    the default property values to use for elements
                    of mesh3d.colorbar.tickformatstops
                ticklabeloverflow
                    Determines how we handle tick labels that would
                    overflow either the graph div or the domain of
                    the axis. The default value for inside tick
                    labels is *hide past domain*. In other cases
                    the default is *hide past div*.
                ticklabelposition
                    Determines where tick labels are drawn relative
                    to the ticks. Left and right options are used
                    when `orientation` is "h", top and bottom when
                    `orientation` is "v".
                ticklen
                    Sets the tick length (in px).
                tickmode
                    Sets the tick mode for this axis. If "auto",
                    the number of ticks is set via `nticks`. If
                    "linear", the placement of the ticks is
                    determined by a starting position `tick0` and a
                    tick step `dtick` ("linear" is the default
                    value if `tick0` and `dtick` are provided). If
                    "array", the placement of the ticks is set via
                    `tickvals` and the tick text is `ticktext`.
                    ("array" is the default value if `tickvals` is
                    provided).
                tickprefix
                    Sets a tick label prefix.
                ticks
                    Determines whether ticks are drawn or not. If
                    "", this axis' ticks are not drawn. If
                    "outside" ("inside"), this axis' are drawn
                    outside (inside) the axis lines.
                ticksuffix
                    Sets a tick label suffix.
                ticktext
                    Sets the text displayed at the ticks position
                    via `tickvals`. Only has an effect if
                    `tickmode` is set to "array". Used with
                    `tickvals`.
                ticktextsrc
                    Sets the source reference on Chart Studio Cloud
                    for `ticktext`.
                tickvals
                    Sets the values at which ticks on this axis
                    appear. Only has an effect if `tickmode` is set
                    to "array". Used with `ticktext`.
                tickvalssrc
                    Sets the source reference on Chart Studio Cloud
                    for `tickvals`.
                tickwidth
                    Sets the tick width (in px).
                title
                    :class:`plotly.graph_objects.mesh3d.colorbar.Ti
                    tle` instance or dict with compatible
                    properties
                titlefont
                    Deprecated: Please use
                    mesh3d.colorbar.title.font instead. Sets this
                    color bar's title font. Note that the title's
                    font used to be set by the now deprecated
                    `titlefont` attribute.
                titleside
                    Deprecated: Please use
                    mesh3d.colorbar.title.side instead. Determines
                    the location of color bar's title with respect
                    to the color bar. Defaults to "top" when
                    `orientation` if "v" and  defaults to "right"
                    when `orientation` if "h". Note that the
                    title's location used to be set by the now
                    deprecated `titleside` attribute.
                x
                    Sets the x position of the color bar (in plot
                    fraction). Defaults to 1.02 when `orientation`
                    is "v" and 0.5 when `orientation` is "h".
                xanchor
                    Sets this color bar's horizontal position
                    anchor. This anchor binds the `x` position to
                    the "left", "center" or "right" of the color
                    bar. Defaults to "left" when `orientation` is
                    "v" and "center" when `orientation` is "h".
                xpad
                    Sets the amount of padding (in px) along the x
                    direction.
                y
                    Sets the y position of the color bar (in plot
                    fraction). Defaults to 0.5 when `orientation`
                    is "v" and 1.02 when `orientation` is "h".
                yanchor
                    Sets this color bar's vertical position anchor
                    This anchor binds the `y` position to the
                    "top", "middle" or "bottom" of the color bar.
                    Defaults to "middle" when `orientation` is "v"
                    and "bottom" when `orientation` is "h".
                ypad
                    Sets the amount of padding (in px) along the y
                    direction.

        Returns
        -------
        plotly.graph_objs.mesh3d.ColorBar
        """
        return self["colorbar"]

    @colorbar.setter
    def colorbar(self, val):
        self["colorbar"] = val

    # colorscale
    # ----------
    @property
    def colorscale(self):
        """
        Sets the colorscale. The colorscale must be an array containing
        arrays mapping a normalized value to an rgb, rgba, hex, hsl,
        hsv, or named color string. At minimum, a mapping for the
        lowest (0) and highest (1) values are required. For example,
        `[[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']]`. To control the
        bounds of the colorscale in color space, use`cmin` and `cmax`.
        Alternatively, `colorscale` may be a palette name string of the
        following list: Blackbody,Bluered,Blues,Cividis,Earth,Electric,
        Greens,Greys,Hot,Jet,Picnic,Portland,Rainbow,RdBu,Reds,Viridis,
        YlGnBu,YlOrRd.
    
        The 'colorscale' property is a colorscale and may be
        specified as:
          - A list of colors that will be spaced evenly to create the colorscale.
            Many predefined colorscale lists are included in the sequential, diverging,
            and cyclical modules in the plotly.colors package.
          - A list of 2-element lists where the first element is the
            normalized color level value (starting at 0 and ending at 1),
            and the second item is a valid color string.
            (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
          - One of the following named colorscales:
                ['aggrnyl', 'agsunset', 'algae', 'amp', 'armyrose', 'balance',
                 'blackbody', 'bluered', 'blues', 'blugrn', 'bluyl', 'brbg',
                 'brwnyl', 'bugn', 'bupu', 'burg', 'burgyl', 'cividis', 'curl',
                 'darkmint', 'deep', 'delta', 'dense', 'earth', 'edge', 'electric',
                 'emrld', 'fall', 'geyser', 'gnbu', 'gray', 'greens', 'greys',
                 'haline', 'hot', 'hsv', 'ice', 'icefire', 'inferno', 'jet',
                 'magenta', 'magma', 'matter', 'mint', 'mrybm', 'mygbm', 'oranges',
                 'orrd', 'oryel', 'oxy', 'peach', 'phase', 'picnic', 'pinkyl',
                 'piyg', 'plasma', 'plotly3', 'portland', 'prgn', 'pubu', 'pubugn',
                 'puor', 'purd', 'purp', 'purples', 'purpor', 'rainbow', 'rdbu',
                 'rdgy', 'rdpu', 'rdylbu', 'rdylgn', 'redor', 'reds', 'solar',
                 'spectral', 'speed', 'sunset', 'sunsetdark', 'teal', 'tealgrn',
                 'tealrose', 'tempo', 'temps', 'thermal', 'tropic', 'turbid',
                 'turbo', 'twilight', 'viridis', 'ylgn', 'ylgnbu', 'ylorbr',
                 'ylorrd'].
            Appending '_r' to a named colorscale reverses it.

        Returns
        -------
        str
        """
        return self["colorscale"]

    @colorscale.setter
    def colorscale(self, val):
        self["colorscale"] = val

    # contour
    # -------
    @property
    def contour(self):
        """
        The 'contour' property is an instance of Contour
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.mesh3d.Contour`
          - A dict of string/value properties that will be passed
            to the Contour constructor
    
            Supported dict properties:
                
                color
                    Sets the color of the contour lines.
                show
                    Sets whether or not dynamic contours are shown
                    on hover
                width
                    Sets the width of the contour lines.

        Returns
        -------
        plotly.graph_objs.mesh3d.Contour
        """
        return self["contour"]

    @contour.setter
    def contour(self, val):
        self["contour"] = val

    # customdata
    # ----------
    @property
    def customdata(self):
        """
        Assigns extra data each datum. This may be useful when
        listening to hover, click and selection events. Note that,
        "scatter" traces also appends customdata items in the markers
        DOM elements
    
        The 'customdata' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["customdata"]

    @customdata.setter
    def customdata(self, val):
        self["customdata"] = val

    # customdatasrc
    # -------------
    @property
    def customdatasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `customdata`.
    
        The 'customdatasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["customdatasrc"]

    @customdatasrc.setter
    def customdatasrc(self, val):
        self["customdatasrc"] = val

    # delaunayaxis
    # ------------
    @property
    def delaunayaxis(self):
        """
        Sets the Delaunay axis, which is the axis that is perpendicular
        to the surface of the Delaunay triangulation. It has an effect
        if `i`, `j`, `k` are not provided and `alphahull` is set to
        indicate Delaunay triangulation.
    
        The 'delaunayaxis' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['x', 'y', 'z']

        Returns
        -------
        Any
        """
        return self["delaunayaxis"]

    @delaunayaxis.setter
    def delaunayaxis(self, val):
        self["delaunayaxis"] = val

    # facecolor
    # ---------
    @property
    def facecolor(self):
        """
        Sets the color of each face Overrides "color" and
        "vertexcolor".
    
        The 'facecolor' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["facecolor"]

    @facecolor.setter
    def facecolor(self, val):
        self["facecolor"] = val

    # facecolorsrc
    # ------------
    @property
    def facecolorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `facecolor`.
    
        The 'facecolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["facecolorsrc"]

    @facecolorsrc.setter
    def facecolorsrc(self, val):
        self["facecolorsrc"] = val

    # flatshading
    # -----------
    @property
    def flatshading(self):
        """
        Determines whether or not normal smoothing is applied to the
        meshes, creating meshes with an angular, low-poly look via flat
        reflections.
    
        The 'flatshading' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["flatshading"]

    @flatshading.setter
    def flatshading(self, val):
        self["flatshading"] = val

    # hoverinfo
    # ---------
    @property
    def hoverinfo(self):
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.
    
        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['x', 'y', 'z', 'text', 'name'] joined with '+' characters
            (e.g. 'x+y')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')
          - A list or array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["hoverinfo"]

    @hoverinfo.setter
    def hoverinfo(self, val):
        self["hoverinfo"] = val

    # hoverinfosrc
    # ------------
    @property
    def hoverinfosrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hoverinfo`.
    
        The 'hoverinfosrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["hoverinfosrc"]

    @hoverinfosrc.setter
    def hoverinfosrc(self, val):
        self["hoverinfosrc"] = val

    # hoverlabel
    # ----------
    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.mesh3d.Hoverlabel`
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor
    
            Supported dict properties:
                
                align
                    Sets the horizontal alignment of the text
                    content within hover label box. Has an effect
                    only if the hover label text spans more two or
                    more lines
                alignsrc
                    Sets the source reference on Chart Studio Cloud
                    for `align`.
                bgcolor
                    Sets the background color of the hover labels
                    for this trace
                bgcolorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `bgcolor`.
                bordercolor
                    Sets the border color of the hover labels for
                    this trace.
                bordercolorsrc
                    Sets the source reference on Chart Studio Cloud
                    for `bordercolor`.
                font
                    Sets the font used in hover labels.
                namelength
                    Sets the default length (in number of
                    characters) of the trace name in the hover
                    labels for all traces. -1 shows the whole name
                    regardless of length. 0-3 shows the first 0-3
                    characters, and an integer >3 will show the
                    whole name if it is less than that many
                    characters, but if it is longer, will truncate
                    to `namelength - 3` characters and add an
                    ellipsis.
                namelengthsrc
                    Sets the source reference on Chart Studio Cloud
                    for `namelength`.

        Returns
        -------
        plotly.graph_objs.mesh3d.Hoverlabel
        """
        return self["hoverlabel"]

    @hoverlabel.setter
    def hoverlabel(self, val):
        self["hoverlabel"] = val

    # hovertemplate
    # -------------
    @property
    def hovertemplate(self):
        """
        Template string used for rendering the information that appear
        on hover box. Note that this will override `hoverinfo`.
        Variables are inserted using %{variable}, for example "y: %{y}"
        as well as %{xother}, {%_xother}, {%_xother_}, {%xother_}. When
        showing info for several points, "xother" will be added to
        those with different x positions from the first point. An
        underscore before or after "(x|y)other" will add a space on
        that side, only when this field is shown. Numbers are formatted
        using d3-format's syntax %{variable:d3-format}, for example
        "Price: %{y:$.2f}".
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format for
        details on the formatting syntax. Dates are formatted using
        d3-time-format's syntax %{variable|d3-time-format}, for example
        "Day: %{2019-01-01|%A}". https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format for details on the date
        formatting syntax. The variables available in `hovertemplate`
        are the ones emitted as event data described at this link
        https://plotly.com/javascript/plotlyjs-events/#event-data.
        Additionally, every attributes that can be specified per-point
        (the ones that are `arrayOk: true`) are available.  Anything
        contained in tag `<extra>` is displayed in the secondary box,
        for example "<extra>{fullData.name}</extra>". To hide the
        secondary box completely, use an empty tag `<extra></extra>`.
    
        The 'hovertemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["hovertemplate"]

    @hovertemplate.setter
    def hovertemplate(self, val):
        self["hovertemplate"] = val

    # hovertemplatesrc
    # ----------------
    @property
    def hovertemplatesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertemplate`.
    
        The 'hovertemplatesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["hovertemplatesrc"]

    @hovertemplatesrc.setter
    def hovertemplatesrc(self, val):
        self["hovertemplatesrc"] = val

    # hovertext
    # ---------
    @property
    def hovertext(self):
        """
        Same as `text`.
    
        The 'hovertext' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["hovertext"]

    @hovertext.setter
    def hovertext(self, val):
        self["hovertext"] = val

    # hovertextsrc
    # ------------
    @property
    def hovertextsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertext`.
    
        The 'hovertextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["hovertextsrc"]

    @hovertextsrc.setter
    def hovertextsrc(self, val):
        self["hovertextsrc"] = val

    # i
    # -
    @property
    def i(self):
        """
        A vector of vertex indices, i.e. integer values between 0 and
        the length of the vertex vectors, representing the "first"
        vertex of a triangle. For example, `{i[m], j[m], k[m]}`
        together represent face m (triangle m) in the mesh, where `i[m]
        = n` points to the triplet `{x[n], y[n], z[n]}` in the vertex
        arrays. Therefore, each element in `i` represents a point in
        space, which is the first vertex of a triangle.
    
        The 'i' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["i"]

    @i.setter
    def i(self, val):
        self["i"] = val

    # ids
    # ---
    @property
    def ids(self):
        """
        Assigns id labels to each datum. These ids for object constancy
        of data points during animation. Should be an array of strings,
        not numbers or any other type.
    
        The 'ids' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["ids"]

    @ids.setter
    def ids(self, val):
        self["ids"] = val

    # idssrc
    # ------
    @property
    def idssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `ids`.
    
        The 'idssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["idssrc"]

    @idssrc.setter
    def idssrc(self, val):
        self["idssrc"] = val

    # intensity
    # ---------
    @property
    def intensity(self):
        """
        Sets the intensity values for vertices or cells as defined by
        `intensitymode`. It can be used for plotting fields on meshes.
    
        The 'intensity' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["intensity"]

    @intensity.setter
    def intensity(self, val):
        self["intensity"] = val

    # intensitymode
    # -------------
    @property
    def intensitymode(self):
        """
        Determines the source of `intensity` values.
    
        The 'intensitymode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['vertex', 'cell']

        Returns
        -------
        Any
        """
        return self["intensitymode"]

    @intensitymode.setter
    def intensitymode(self, val):
        self["intensitymode"] = val

    # intensitysrc
    # ------------
    @property
    def intensitysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `intensity`.
    
        The 'intensitysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["intensitysrc"]

    @intensitysrc.setter
    def intensitysrc(self, val):
        self["intensitysrc"] = val

    # isrc
    # ----
    @property
    def isrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `i`.
    
        The 'isrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["isrc"]

    @isrc.setter
    def isrc(self, val):
        self["isrc"] = val

    # j
    # -
    @property
    def j(self):
        """
        A vector of vertex indices, i.e. integer values between 0 and
        the length of the vertex vectors, representing the "second"
        vertex of a triangle. For example, `{i[m], j[m], k[m]}`
        together represent face m (triangle m) in the mesh, where `j[m]
        = n` points to the triplet `{x[n], y[n], z[n]}` in the vertex
        arrays. Therefore, each element in `j` represents a point in
        space, which is the second vertex of a triangle.
    
        The 'j' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["j"]

    @j.setter
    def j(self, val):
        self["j"] = val

    # jsrc
    # ----
    @property
    def jsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `j`.
    
        The 'jsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["jsrc"]

    @jsrc.setter
    def jsrc(self, val):
        self["jsrc"] = val

    # k
    # -
    @property
    def k(self):
        """
        A vector of vertex indices, i.e. integer values between 0 and
        the length of the vertex vectors, representing the "third"
        vertex of a triangle. For example, `{i[m], j[m], k[m]}`
        together represent face m (triangle m) in the mesh, where `k[m]
        = n` points to the triplet  `{x[n], y[n], z[n]}` in the vertex
        arrays. Therefore, each element in `k` represents a point in
        space, which is the third vertex of a triangle.
    
        The 'k' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["k"]

    @k.setter
    def k(self, val):
        self["k"] = val

    # ksrc
    # ----
    @property
    def ksrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `k`.
    
        The 'ksrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["ksrc"]

    @ksrc.setter
    def ksrc(self, val):
        self["ksrc"] = val

    # legendgroup
    # -----------
    @property
    def legendgroup(self):
        """
        Sets the legend group for this trace. Traces part of the same
        legend group hide/show at the same time when toggling legend
        items.
    
        The 'legendgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["legendgroup"]

    @legendgroup.setter
    def legendgroup(self, val):
        self["legendgroup"] = val

    # legendgrouptitle
    # ----------------
    @property
    def legendgrouptitle(self):
        """
        The 'legendgrouptitle' property is an instance of Legendgrouptitle
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.mesh3d.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor
    
            Supported dict properties:
                
                font
                    Sets this legend group's title font.
                text
                    Sets the title of the legend group.

        Returns
        -------
        plotly.graph_objs.mesh3d.Legendgrouptitle
        """
        return self["legendgrouptitle"]

    @legendgrouptitle.setter
    def legendgrouptitle(self, val):
        self["legendgrouptitle"] = val

    # legendrank
    # ----------
    @property
    def legendrank(self):
        """
        Sets the legend rank for this trace. Items and groups with
        smaller ranks are presented on top/left side while with
        `*reversed* `legend.traceorder` they are on bottom/right side.
        The default legendrank is 1000, so that you can use ranks less
        than 1000 to place certain items before all unranked items, and
        ranks greater than 1000 to go after all unranked items.
    
        The 'legendrank' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self["legendrank"]

    @legendrank.setter
    def legendrank(self, val):
        self["legendrank"] = val

    # lighting
    # --------
    @property
    def lighting(self):
        """
        The 'lighting' property is an instance of Lighting
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.mesh3d.Lighting`
          - A dict of string/value properties that will be passed
            to the Lighting constructor
    
            Supported dict properties:
                
                ambient
                    Ambient light increases overall color
                    visibility but can wash out the image.
                diffuse
                    Represents the extent that incident rays are
                    reflected in a range of angles.
                facenormalsepsilon
                    Epsilon for face normals calculation avoids
                    math issues arising from degenerate geometry.
                fresnel
                    Represents the reflectance as a dependency of
                    the viewing angle; e.g. paper is reflective
                    when viewing it from the edge of the paper
                    (almost 90 degrees), causing shine.
                roughness
                    Alters specular reflection; the rougher the
                    surface, the wider and less contrasty the
                    shine.
                specular
                    Represents the level that incident rays are
                    reflected in a single direction, causing shine.
                vertexnormalsepsilon
                    Epsilon for vertex normals calculation avoids
                    math issues arising from degenerate geometry.

        Returns
        -------
        plotly.graph_objs.mesh3d.Lighting
        """
        return self["lighting"]

    @lighting.setter
    def lighting(self, val):
        self["lighting"] = val

    # lightposition
    # -------------
    @property
    def lightposition(self):
        """
        The 'lightposition' property is an instance of Lightposition
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.mesh3d.Lightposition`
          - A dict of string/value properties that will be passed
            to the Lightposition constructor
    
            Supported dict properties:
                
                x
                    Numeric vector, representing the X coordinate
                    for each vertex.
                y
                    Numeric vector, representing the Y coordinate
                    for each vertex.
                z
                    Numeric vector, representing the Z coordinate
                    for each vertex.

        Returns
        -------
        plotly.graph_objs.mesh3d.Lightposition
        """
        return self["lightposition"]

    @lightposition.setter
    def lightposition(self, val):
        self["lightposition"] = val

    # meta
    # ----
    @property
    def meta(self):
        """
        Assigns extra meta information associated with this trace that
        can be used in various text attributes. Attributes such as
        trace `name`, graph, axis and colorbar `title.text`, annotation
        `text` `rangeselector`, `updatemenues` and `sliders` `label`
        text all support `meta`. To access the trace `meta` values in
        an attribute in the same trace, simply use `%{meta[i]}` where
        `i` is the index or key of the `meta` item in question. To
        access trace `meta` in layout attributes, use
        `%{data[n[.meta[i]}` where `i` is the index or key of the
        `meta` and `n` is the trace index.
    
        The 'meta' property accepts values of any type

        Returns
        -------
        Any|numpy.ndarray
        """
        return self["meta"]

    @meta.setter
    def meta(self, val):
        self["meta"] = val

    # metasrc
    # -------
    @property
    def metasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `meta`.
    
        The 'metasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["metasrc"]

    @metasrc.setter
    def metasrc(self, val):
        self["metasrc"] = val

    # name
    # ----
    @property
    def name(self):
        """
        Sets the trace name. The trace name appear as the legend item
        and on hover.
    
        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["name"]

    @name.setter
    def name(self, val):
        self["name"] = val

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the opacity of the surface. Please note that in the case
        of using high `opacity` values for example a value greater than
        or equal to 0.5 on two surfaces (and 0.25 with four surfaces),
        an overlay of multiple transparent surfaces may not perfectly
        be sorted in depth by the webgl API. This behavior may be
        improved in the near future and is subject to change.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["opacity"]

    @opacity.setter
    def opacity(self, val):
        self["opacity"] = val

    # reversescale
    # ------------
    @property
    def reversescale(self):
        """
        Reverses the color mapping if true. If true, `cmin` will
        correspond to the last color in the array and `cmax` will
        correspond to the first color.
    
        The 'reversescale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["reversescale"]

    @reversescale.setter
    def reversescale(self, val):
        self["reversescale"] = val

    # scene
    # -----
    @property
    def scene(self):
        """
        Sets a reference between this trace's 3D coordinate system and
        a 3D scene. If "scene" (the default value), the (x,y,z)
        coordinates refer to `layout.scene`. If "scene2", the (x,y,z)
        coordinates refer to `layout.scene2`, and so on.
    
        The 'scene' property is an identifier of a particular
        subplot, of type 'scene', that may be specified as the string 'scene'
        optionally followed by an integer >= 1
        (e.g. 'scene', 'scene1', 'scene2', 'scene3', etc.)

        Returns
        -------
        str
        """
        return self["scene"]

    @scene.setter
    def scene(self, val):
        self["scene"] = val

    # showlegend
    # ----------
    @property
    def showlegend(self):
        """
        Determines whether or not an item corresponding to this trace
        is shown in the legend.
    
        The 'showlegend' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showlegend"]

    @showlegend.setter
    def showlegend(self, val):
        self["showlegend"] = val

    # showscale
    # ---------
    @property
    def showscale(self):
        """
        Determines whether or not a colorbar is displayed for this
        trace.
    
        The 'showscale' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["showscale"]

    @showscale.setter
    def showscale(self, val):
        self["showscale"] = val

    # stream
    # ------
    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.mesh3d.Stream`
          - A dict of string/value properties that will be passed
            to the Stream constructor
    
            Supported dict properties:
                
                maxpoints
                    Sets the maximum number of points to keep on
                    the plots from an incoming stream. If
                    `maxpoints` is set to 50, only the newest 50
                    points will be displayed on the plot.
                token
                    The stream id number links a data trace on a
                    plot with a stream. See https://chart-
                    studio.plotly.com/settings for more details.

        Returns
        -------
        plotly.graph_objs.mesh3d.Stream
        """
        return self["stream"]

    @stream.setter
    def stream(self, val):
        self["stream"] = val

    # text
    # ----
    @property
    def text(self):
        """
        Sets the text elements associated with the vertices. If trace
        `hoverinfo` contains a "text" flag and "hovertext" is not set,
        these elements will be seen in the hover labels.
    
        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self["text"]

    @text.setter
    def text(self, val):
        self["text"] = val

    # textsrc
    # -------
    @property
    def textsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `text`.
    
        The 'textsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["textsrc"]

    @textsrc.setter
    def textsrc(self, val):
        self["textsrc"] = val

    # uid
    # ---
    @property
    def uid(self):
        """
        Assign an id to this trace, Use this to provide object
        constancy between traces during animations and transitions.
    
        The 'uid' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["uid"]

    @uid.setter
    def uid(self, val):
        self["uid"] = val

    # uirevision
    # ----------
    @property
    def uirevision(self):
        """
        Controls persistence of some user-driven changes to the trace:
        `constraintrange` in `parcoords` traces, as well as some
        `editable: true` modifications such as `name` and
        `colorbar.title`. Defaults to `layout.uirevision`. Note that
        other user-driven trace attribute changes are controlled by
        `layout` attributes: `trace.visible` is controlled by
        `layout.legend.uirevision`, `selectedpoints` is controlled by
        `layout.selectionrevision`, and `colorbar.(x|y)` (accessible
        with `config: {editable: true}`) is controlled by
        `layout.editrevision`. Trace changes are tracked by `uid`,
        which only falls back on trace index if no `uid` is provided.
        So if your app can add/remove traces before the end of the
        `data` array, such that the same trace has a different index,
        you can still preserve user-driven changes if you give each
        trace a `uid` that stays with it as it moves.
    
        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    # vertexcolor
    # -----------
    @property
    def vertexcolor(self):
        """
        Sets the color of each vertex Overrides "color". While Red,
        green and blue colors are in the range of 0 and 255; in the
        case of having vertex color data in RGBA format, the alpha
        color should be normalized to be between 0 and 1.
    
        The 'vertexcolor' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["vertexcolor"]

    @vertexcolor.setter
    def vertexcolor(self, val):
        self["vertexcolor"] = val

    # vertexcolorsrc
    # --------------
    @property
    def vertexcolorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `vertexcolor`.
    
        The 'vertexcolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["vertexcolorsrc"]

    @vertexcolorsrc.setter
    def vertexcolorsrc(self, val):
        self["vertexcolorsrc"] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this trace is visible. If
        "legendonly", the trace is not drawn, but can appear as a
        legend item (provided that the legend itself is visible).
    
        The 'visible' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'legendonly']

        Returns
        -------
        Any
        """
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    # x
    # -
    @property
    def x(self):
        """
        Sets the X coordinates of the vertices. The nth element of
        vectors `x`, `y` and `z` jointly represent the X, Y and Z
        coordinates of the nth vertex.
    
        The 'x' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["x"]

    @x.setter
    def x(self, val):
        self["x"] = val

    # xcalendar
    # ---------
    @property
    def xcalendar(self):
        """
        Sets the calendar system to use with `x` date data.
    
        The 'xcalendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['chinese', 'coptic', 'discworld', 'ethiopian',
                'gregorian', 'hebrew', 'islamic', 'jalali', 'julian',
                'mayan', 'nanakshahi', 'nepali', 'persian', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        return self["xcalendar"]

    @xcalendar.setter
    def xcalendar(self, val):
        self["xcalendar"] = val

    # xhoverformat
    # ------------
    @property
    def xhoverformat(self):
        """
        Sets the hover text formatting rulefor `x`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `xaxis.hoverformat`.
    
        The 'xhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["xhoverformat"]

    @xhoverformat.setter
    def xhoverformat(self, val):
        self["xhoverformat"] = val

    # xsrc
    # ----
    @property
    def xsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `x`.
    
        The 'xsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["xsrc"]

    @xsrc.setter
    def xsrc(self, val):
        self["xsrc"] = val

    # y
    # -
    @property
    def y(self):
        """
        Sets the Y coordinates of the vertices. The nth element of
        vectors `x`, `y` and `z` jointly represent the X, Y and Z
        coordinates of the nth vertex.
    
        The 'y' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["y"]

    @y.setter
    def y(self, val):
        self["y"] = val

    # ycalendar
    # ---------
    @property
    def ycalendar(self):
        """
        Sets the calendar system to use with `y` date data.
    
        The 'ycalendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['chinese', 'coptic', 'discworld', 'ethiopian',
                'gregorian', 'hebrew', 'islamic', 'jalali', 'julian',
                'mayan', 'nanakshahi', 'nepali', 'persian', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        return self["ycalendar"]

    @ycalendar.setter
    def ycalendar(self, val):
        self["ycalendar"] = val

    # yhoverformat
    # ------------
    @property
    def yhoverformat(self):
        """
        Sets the hover text formatting rulefor `y`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `yaxis.hoverformat`.
    
        The 'yhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["yhoverformat"]

    @yhoverformat.setter
    def yhoverformat(self, val):
        self["yhoverformat"] = val

    # ysrc
    # ----
    @property
    def ysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `y`.
    
        The 'ysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["ysrc"]

    @ysrc.setter
    def ysrc(self, val):
        self["ysrc"] = val

    # z
    # -
    @property
    def z(self):
        """
        Sets the Z coordinates of the vertices. The nth element of
        vectors `x`, `y` and `z` jointly represent the X, Y and Z
        coordinates of the nth vertex.
    
        The 'z' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self["z"]

    @z.setter
    def z(self, val):
        self["z"] = val

    # zcalendar
    # ---------
    @property
    def zcalendar(self):
        """
        Sets the calendar system to use with `z` date data.
    
        The 'zcalendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['chinese', 'coptic', 'discworld', 'ethiopian',
                'gregorian', 'hebrew', 'islamic', 'jalali', 'julian',
                'mayan', 'nanakshahi', 'nepali', 'persian', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        return self["zcalendar"]

    @zcalendar.setter
    def zcalendar(self, val):
        self["zcalendar"] = val

    # zhoverformat
    # ------------
    @property
    def zhoverformat(self):
        """
        Sets the hover text formatting rulefor `z`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `zaxis.hoverformat`.
    
        The 'zhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self["zhoverformat"]

    @zhoverformat.setter
    def zhoverformat(self, val):
        self["zhoverformat"] = val

    # zsrc
    # ----
    @property
    def zsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `z`.
    
        The 'zsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self["zsrc"]

    @zsrc.setter
    def zsrc(self, val):
        self["zsrc"] = val

    # type
    # ----
    @property
    def type(self):
        return self._props["type"]

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        alphahull
            Determines how the mesh surface triangles are derived
            from the set of vertices (points) represented by the
            `x`, `y` and `z` arrays, if the `i`, `j`, `k` arrays
            are not supplied. For general use of `mesh3d` it is
            preferred that `i`, `j`, `k` are supplied. If "-1",
            Delaunay triangulation is used, which is mainly
            suitable if the mesh is a single, more or less layer
            surface that is perpendicular to `delaunayaxis`. In
            case the `delaunayaxis` intersects the mesh surface at
            more than one point it will result triangles that are
            very long in the dimension of `delaunayaxis`. If ">0",
            the alpha-shape algorithm is used. In this case, the
            positive `alphahull` value signals the use of the
            alpha-shape algorithm, _and_ its value acts as the
            parameter for the mesh fitting. If 0,  the convex-hull
            algorithm is used. It is suitable for convex bodies or
            if the intention is to enclose the `x`, `y` and `z`
            point set into a convex hull.
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here `intensity`) or
            the bounds set in `cmin` and `cmax`  Defaults to
            `false` when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as `intensity` and if set, `cmin`
            must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as `intensity`. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as `intensity` and if set, `cmax`
            must be set as well.
        color
            Sets the color of the whole mesh
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.mesh3d.ColorBar` instance
            or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Blackbody,Bluered,Blues,C
            ividis,Earth,Electric,Greens,Greys,Hot,Jet,Picnic,Portl
            and,Rainbow,RdBu,Reds,Viridis,YlGnBu,YlOrRd.
        contour
            :class:`plotly.graph_objects.mesh3d.Contour` instance
            or dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        delaunayaxis
            Sets the Delaunay axis, which is the axis that is
            perpendicular to the surface of the Delaunay
            triangulation. It has an effect if `i`, `j`, `k` are
            not provided and `alphahull` is set to indicate
            Delaunay triangulation.
        facecolor
            Sets the color of each face Overrides "color" and
            "vertexcolor".
        facecolorsrc
            Sets the source reference on Chart Studio Cloud for
            `facecolor`.
        flatshading
            Determines whether or not normal smoothing is applied
            to the meshes, creating meshes with an angular, low-
            poly look via flat reflections.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.mesh3d.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            `hovertext`.
        i
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the "first" vertex of a triangle. For example, `{i[m],
            j[m], k[m]}` together represent face m (triangle m) in
            the mesh, where `i[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `i` represents a point in space, which
            is the first vertex of a triangle.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        intensity
            Sets the intensity values for vertices or cells as
            defined by `intensitymode`. It can be used for plotting
            fields on meshes.
        intensitymode
            Determines the source of `intensity` values.
        intensitysrc
            Sets the source reference on Chart Studio Cloud for
            `intensity`.
        isrc
            Sets the source reference on Chart Studio Cloud for
            `i`.
        j
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the "second" vertex of a triangle. For example, `{i[m],
            j[m], k[m]}`  together represent face m (triangle m) in
            the mesh, where `j[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `j` represents a point in space, which
            is the second vertex of a triangle.
        jsrc
            Sets the source reference on Chart Studio Cloud for
            `j`.
        k
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the "third" vertex of a triangle. For example, `{i[m],
            j[m], k[m]}` together represent face m (triangle m) in
            the mesh, where `k[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `k` represents a point in space, which
            is the third vertex of a triangle.
        ksrc
            Sets the source reference on Chart Studio Cloud for
            `k`.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        legendgrouptitle
            :class:`plotly.graph_objects.mesh3d.Legendgrouptitle`
            instance or dict with compatible properties
        legendrank
            Sets the legend rank for this trace. Items and groups
            with smaller ranks are presented on top/left side while
            with `*reversed* `legend.traceorder` they are on
            bottom/right side. The default legendrank is 1000, so
            that you can use ranks less than 1000 to place certain
            items before all unranked items, and ranks greater than
            1000 to go after all unranked items.
        lighting
            :class:`plotly.graph_objects.mesh3d.Lighting` instance
            or dict with compatible properties
        lightposition
            :class:`plotly.graph_objects.mesh3d.Lightposition`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            `meta`.
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.mesh3d.Stream` instance or
            dict with compatible properties
        text
            Sets the text elements associated with the vertices. If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            `text`.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        vertexcolor
            Sets the color of each vertex Overrides "color". While
            Red, green and blue colors are in the range of 0 and
            255; in the case of having vertex color data in RGBA
            format, the alpha color should be normalized to be
            between 0 and 1.
        vertexcolorsrc
            Sets the source reference on Chart Studio Cloud for
            `vertexcolor`.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the X coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xhoverformat
            Sets the hover text formatting rulefor `x`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `xaxis.hoverformat`.
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            Sets the Y coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        ycalendar
            Sets the calendar system to use with `y` date data.
        yhoverformat
            Sets the hover text formatting rulefor `y`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `yaxis.hoverformat`.
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.
        z
            Sets the Z coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        zcalendar
            Sets the calendar system to use with `z` date data.
        zhoverformat
            Sets the hover text formatting rulefor `z`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `zaxis.hoverformat`.
        zsrc
            Sets the source reference on Chart Studio Cloud for
            `z`.
        """

    def __init__(
        self,
        arg=None,
        alphahull=None,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        color=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contour=None,
        customdata=None,
        customdatasrc=None,
        delaunayaxis=None,
        facecolor=None,
        facecolorsrc=None,
        flatshading=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        i=None,
        ids=None,
        idssrc=None,
        intensity=None,
        intensitymode=None,
        intensitysrc=None,
        isrc=None,
        j=None,
        jsrc=None,
        k=None,
        ksrc=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        vertexcolor=None,
        vertexcolorsrc=None,
        visible=None,
        x=None,
        xcalendar=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        ycalendar=None,
        yhoverformat=None,
        ysrc=None,
        z=None,
        zcalendar=None,
        zhoverformat=None,
        zsrc=None,
        **kwargs
    ):
        """
        Construct a new Mesh3d object
        
        Draws sets of triangles with coordinates given by three
        1-dimensional arrays in `x`, `y`, `z` and (1) a sets of `i`,
        `j`, `k` indices (2) Delaunay triangulation or (3) the Alpha-
        shape algorithm or (4) the Convex-hull algorithm

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Mesh3d`
        alphahull
            Determines how the mesh surface triangles are derived
            from the set of vertices (points) represented by the
            `x`, `y` and `z` arrays, if the `i`, `j`, `k` arrays
            are not supplied. For general use of `mesh3d` it is
            preferred that `i`, `j`, `k` are supplied. If "-1",
            Delaunay triangulation is used, which is mainly
            suitable if the mesh is a single, more or less layer
            surface that is perpendicular to `delaunayaxis`. In
            case the `delaunayaxis` intersects the mesh surface at
            more than one point it will result triangles that are
            very long in the dimension of `delaunayaxis`. If ">0",
            the alpha-shape algorithm is used. In this case, the
            positive `alphahull` value signals the use of the
            alpha-shape algorithm, _and_ its value acts as the
            parameter for the mesh fitting. If 0,  the convex-hull
            algorithm is used. It is suitable for convex bodies or
            if the intention is to enclose the `x`, `y` and `z`
            point set into a convex hull.
        autocolorscale
            Determines whether the colorscale is a default palette
            (`autocolorscale: true`) or the palette determined by
            `colorscale`. In case `colorscale` is unspecified or
            `autocolorscale` is true, the default  palette will be
            chosen according to whether numbers in the `color`
            array are all positive, all negative or mixed.
        cauto
            Determines whether or not the color domain is computed
            with respect to the input data (here `intensity`) or
            the bounds set in `cmin` and `cmax`  Defaults to
            `false` when `cmin` and `cmax` are set by the user.
        cmax
            Sets the upper bound of the color domain. Value should
            have the same units as `intensity` and if set, `cmin`
            must be set as well.
        cmid
            Sets the mid-point of the color domain by scaling
            `cmin` and/or `cmax` to be equidistant to this point.
            Value should have the same units as `intensity`. Has no
            effect when `cauto` is `false`.
        cmin
            Sets the lower bound of the color domain. Value should
            have the same units as `intensity` and if set, `cmax`
            must be set as well.
        color
            Sets the color of the whole mesh
        coloraxis
            Sets a reference to a shared color axis. References to
            these shared color axes are "coloraxis", "coloraxis2",
            "coloraxis3", etc. Settings for these shared color axes
            are set in the layout, under `layout.coloraxis`,
            `layout.coloraxis2`, etc. Note that multiple color
            scales can be linked to the same color axis.
        colorbar
            :class:`plotly.graph_objects.mesh3d.ColorBar` instance
            or dict with compatible properties
        colorscale
            Sets the colorscale. The colorscale must be an array
            containing arrays mapping a normalized value to an rgb,
            rgba, hex, hsl, hsv, or named color string. At minimum,
            a mapping for the lowest (0) and highest (1) values are
            required. For example, `[[0, 'rgb(0,0,255)'], [1,
            'rgb(255,0,0)']]`. To control the bounds of the
            colorscale in color space, use`cmin` and `cmax`.
            Alternatively, `colorscale` may be a palette name
            string of the following list: Blackbody,Bluered,Blues,C
            ividis,Earth,Electric,Greens,Greys,Hot,Jet,Picnic,Portl
            and,Rainbow,RdBu,Reds,Viridis,YlGnBu,YlOrRd.
        contour
            :class:`plotly.graph_objects.mesh3d.Contour` instance
            or dict with compatible properties
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        delaunayaxis
            Sets the Delaunay axis, which is the axis that is
            perpendicular to the surface of the Delaunay
            triangulation. It has an effect if `i`, `j`, `k` are
            not provided and `alphahull` is set to indicate
            Delaunay triangulation.
        facecolor
            Sets the color of each face Overrides "color" and
            "vertexcolor".
        facecolorsrc
            Sets the source reference on Chart Studio Cloud for
            `facecolor`.
        flatshading
            Determines whether or not normal smoothing is applied
            to the meshes, creating meshes with an angular, low-
            poly look via flat reflections.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.mesh3d.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, every attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            "<extra>{fullData.name}</extra>". To hide the secondary
            box completely, use an empty tag `<extra></extra>`.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        hovertext
            Same as `text`.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            `hovertext`.
        i
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the "first" vertex of a triangle. For example, `{i[m],
            j[m], k[m]}` together represent face m (triangle m) in
            the mesh, where `i[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `i` represents a point in space, which
            is the first vertex of a triangle.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        intensity
            Sets the intensity values for vertices or cells as
            defined by `intensitymode`. It can be used for plotting
            fields on meshes.
        intensitymode
            Determines the source of `intensity` values.
        intensitysrc
            Sets the source reference on Chart Studio Cloud for
            `intensity`.
        isrc
            Sets the source reference on Chart Studio Cloud for
            `i`.
        j
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the "second" vertex of a triangle. For example, `{i[m],
            j[m], k[m]}`  together represent face m (triangle m) in
            the mesh, where `j[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `j` represents a point in space, which
            is the second vertex of a triangle.
        jsrc
            Sets the source reference on Chart Studio Cloud for
            `j`.
        k
            A vector of vertex indices, i.e. integer values between
            0 and the length of the vertex vectors, representing
            the "third" vertex of a triangle. For example, `{i[m],
            j[m], k[m]}` together represent face m (triangle m) in
            the mesh, where `k[m] = n` points to the triplet
            `{x[n], y[n], z[n]}` in the vertex arrays. Therefore,
            each element in `k` represents a point in space, which
            is the third vertex of a triangle.
        ksrc
            Sets the source reference on Chart Studio Cloud for
            `k`.
        legendgroup
            Sets the legend group for this trace. Traces part of
            the same legend group hide/show at the same time when
            toggling legend items.
        legendgrouptitle
            :class:`plotly.graph_objects.mesh3d.Legendgrouptitle`
            instance or dict with compatible properties
        legendrank
            Sets the legend rank for this trace. Items and groups
            with smaller ranks are presented on top/left side while
            with `*reversed* `legend.traceorder` they are on
            bottom/right side. The default legendrank is 1000, so
            that you can use ranks less than 1000 to place certain
            items before all unranked items, and ranks greater than
            1000 to go after all unranked items.
        lighting
            :class:`plotly.graph_objects.mesh3d.Lighting` instance
            or dict with compatible properties
        lightposition
            :class:`plotly.graph_objects.mesh3d.Lightposition`
            instance or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            `meta`.
        name
            Sets the trace name. The trace name appear as the
            legend item and on hover.
        opacity
            Sets the opacity of the surface. Please note that in
            the case of using high `opacity` values for example a
            value greater than or equal to 0.5 on two surfaces (and
            0.25 with four surfaces), an overlay of multiple
            transparent surfaces may not perfectly be sorted in
            depth by the webgl API. This behavior may be improved
            in the near future and is subject to change.
        reversescale
            Reverses the color mapping if true. If true, `cmin`
            will correspond to the last color in the array and
            `cmax` will correspond to the first color.
        scene
            Sets a reference between this trace's 3D coordinate
            system and a 3D scene. If "scene" (the default value),
            the (x,y,z) coordinates refer to `layout.scene`. If
            "scene2", the (x,y,z) coordinates refer to
            `layout.scene2`, and so on.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        showscale
            Determines whether or not a colorbar is displayed for
            this trace.
        stream
            :class:`plotly.graph_objects.mesh3d.Stream` instance or
            dict with compatible properties
        text
            Sets the text elements associated with the vertices. If
            trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            `text`.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        vertexcolor
            Sets the color of each vertex Overrides "color". While
            Red, green and blue colors are in the range of 0 and
            255; in the case of having vertex color data in RGBA
            format, the alpha color should be normalized to be
            between 0 and 1.
        vertexcolorsrc
            Sets the source reference on Chart Studio Cloud for
            `vertexcolor`.
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the X coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xhoverformat
            Sets the hover text formatting rulefor `x`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `xaxis.hoverformat`.
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            Sets the Y coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        ycalendar
            Sets the calendar system to use with `y` date data.
        yhoverformat
            Sets the hover text formatting rulefor `y`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `yaxis.hoverformat`.
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.
        z
            Sets the Z coordinates of the vertices. The nth element
            of vectors `x`, `y` and `z` jointly represent the X, Y
            and Z coordinates of the nth vertex.
        zcalendar
            Sets the calendar system to use with `z` date data.
        zhoverformat
            Sets the hover text formatting rulefor `z`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `zaxis.hoverformat`.
        zsrc
            Sets the source reference on Chart Studio Cloud for
            `z`.

        Returns
        -------
        Mesh3d
        """
        super(Mesh3d, self).__init__("mesh3d")

        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.Mesh3d 
constructor must be a dict or 
an instance of :class:`plotly.graph_objs.Mesh3d`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("alphahull", None)
        _v = alphahull if alphahull is not None else _v
        if _v is not None:
            self["alphahull"] = _v
        _v = arg.pop("autocolorscale", None)
        _v = autocolorscale if autocolorscale is not None else _v
        if _v is not None:
            self["autocolorscale"] = _v
        _v = arg.pop("cauto", None)
        _v = cauto if cauto is not None else _v
        if _v is not None:
            self["cauto"] = _v
        _v = arg.pop("cmax", None)
        _v = cmax if cmax is not None else _v
        if _v is not None:
            self["cmax"] = _v
        _v = arg.pop("cmid", None)
        _v = cmid if cmid is not None else _v
        if _v is not None:
            self["cmid"] = _v
        _v = arg.pop("cmin", None)
        _v = cmin if cmin is not None else _v
        if _v is not None:
            self["cmin"] = _v
        _v = arg.pop("color", None)
        _v = color if color is not None else _v
        if _v is not None:
            self["color"] = _v
        _v = arg.pop("coloraxis", None)
        _v = coloraxis if coloraxis is not None else _v
        if _v is not None:
            self["coloraxis"] = _v
        _v = arg.pop("colorbar", None)
        _v = colorbar if colorbar is not None else _v
        if _v is not None:
            self["colorbar"] = _v
        _v = arg.pop("colorscale", None)
        _v = colorscale if colorscale is not None else _v
        if _v is not None:
            self["colorscale"] = _v
        _v = arg.pop("contour", None)
        _v = contour if contour is not None else _v
        if _v is not None:
            self["contour"] = _v
        _v = arg.pop("customdata", None)
        _v = customdata if customdata is not None else _v
        if _v is not None:
            self["customdata"] = _v
        _v = arg.pop("customdatasrc", None)
        _v = customdatasrc if customdatasrc is not None else _v
        if _v is not None:
            self["customdatasrc"] = _v
        _v = arg.pop("delaunayaxis", None)
        _v = delaunayaxis if delaunayaxis is not None else _v
        if _v is not None:
            self["delaunayaxis"] = _v
        _v = arg.pop("facecolor", None)
        _v = facecolor if facecolor is not None else _v
        if _v is not None:
            self["facecolor"] = _v
        _v = arg.pop("facecolorsrc", None)
        _v = facecolorsrc if facecolorsrc is not None else _v
        if _v is not None:
            self["facecolorsrc"] = _v
        _v = arg.pop("flatshading", None)
        _v = flatshading if flatshading is not None else _v
        if _v is not None:
            self["flatshading"] = _v
        _v = arg.pop("hoverinfo", None)
        _v = hoverinfo if hoverinfo is not None else _v
        if _v is not None:
            self["hoverinfo"] = _v
        _v = arg.pop("hoverinfosrc", None)
        _v = hoverinfosrc if hoverinfosrc is not None else _v
        if _v is not None:
            self["hoverinfosrc"] = _v
        _v = arg.pop("hoverlabel", None)
        _v = hoverlabel if hoverlabel is not None else _v
        if _v is not None:
            self["hoverlabel"] = _v
        _v = arg.pop("hovertemplate", None)
        _v = hovertemplate if hovertemplate is not None else _v
        if _v is not None:
            self["hovertemplate"] = _v
        _v = arg.pop("hovertemplatesrc", None)
        _v = hovertemplatesrc if hovertemplatesrc is not None else _v
        if _v is not None:
            self["hovertemplatesrc"] = _v
        _v = arg.pop("hovertext", None)
        _v = hovertext if hovertext is not None else _v
        if _v is not None:
            self["hovertext"] = _v
        _v = arg.pop("hovertextsrc", None)
        _v = hovertextsrc if hovertextsrc is not None else _v
        if _v is not None:
            self["hovertextsrc"] = _v
        _v = arg.pop("i", None)
        _v = i if i is not None else _v
        if _v is not None:
            self["i"] = _v
        _v = arg.pop("ids", None)
        _v = ids if ids is not None else _v
        if _v is not None:
            self["ids"] = _v
        _v = arg.pop("idssrc", None)
        _v = idssrc if idssrc is not None else _v
        if _v is not None:
            self["idssrc"] = _v
        _v = arg.pop("intensity", None)
        _v = intensity if intensity is not None else _v
        if _v is not None:
            self["intensity"] = _v
        _v = arg.pop("intensitymode", None)
        _v = intensitymode if intensitymode is not None else _v
        if _v is not None:
            self["intensitymode"] = _v
        _v = arg.pop("intensitysrc", None)
        _v = intensitysrc if intensitysrc is not None else _v
        if _v is not None:
            self["intensitysrc"] = _v
        _v = arg.pop("isrc", None)
        _v = isrc if isrc is not None else _v
        if _v is not None:
            self["isrc"] = _v
        _v = arg.pop("j", None)
        _v = j if j is not None else _v
        if _v is not None:
            self["j"] = _v
        _v = arg.pop("jsrc", None)
        _v = jsrc if jsrc is not None else _v
        if _v is not None:
            self["jsrc"] = _v
        _v = arg.pop("k", None)
        _v = k if k is not None else _v
        if _v is not None:
            self["k"] = _v
        _v = arg.pop("ksrc", None)
        _v = ksrc if ksrc is not None else _v
        if _v is not None:
            self["ksrc"] = _v
        _v = arg.pop("legendgroup", None)
        _v = legendgroup if legendgroup is not None else _v
        if _v is not None:
            self["legendgroup"] = _v
        _v = arg.pop("legendgrouptitle", None)
        _v = legendgrouptitle if legendgrouptitle is not None else _v
        if _v is not None:
            self["legendgrouptitle"] = _v
        _v = arg.pop("legendrank", None)
        _v = legendrank if legendrank is not None else _v
        if _v is not None:
            self["legendrank"] = _v
        _v = arg.pop("lighting", None)
        _v = lighting if lighting is not None else _v
        if _v is not None:
            self["lighting"] = _v
        _v = arg.pop("lightposition", None)
        _v = lightposition if lightposition is not None else _v
        if _v is not None:
            self["lightposition"] = _v
        _v = arg.pop("meta", None)
        _v = meta if meta is not None else _v
        if _v is not None:
            self["meta"] = _v
        _v = arg.pop("metasrc", None)
        _v = metasrc if metasrc is not None else _v
        if _v is not None:
            self["metasrc"] = _v
        _v = arg.pop("name", None)
        _v = name if name is not None else _v
        if _v is not None:
            self["name"] = _v
        _v = arg.pop("opacity", None)
        _v = opacity if opacity is not None else _v
        if _v is not None:
            self["opacity"] = _v
        _v = arg.pop("reversescale", None)
        _v = reversescale if reversescale is not None else _v
        if _v is not None:
            self["reversescale"] = _v
        _v = arg.pop("scene", None)
        _v = scene if scene is not None else _v
        if _v is not None:
            self["scene"] = _v
        _v = arg.pop("showlegend", None)
        _v = showlegend if showlegend is not None else _v
        if _v is not None:
            self["showlegend"] = _v
        _v = arg.pop("showscale", None)
        _v = showscale if showscale is not None else _v
        if _v is not None:
            self["showscale"] = _v
        _v = arg.pop("stream", None)
        _v = stream if stream is not None else _v
        if _v is not None:
            self["stream"] = _v
        _v = arg.pop("text", None)
        _v = text if text is not None else _v
        if _v is not None:
            self["text"] = _v
        _v = arg.pop("textsrc", None)
        _v = textsrc if textsrc is not None else _v
        if _v is not None:
            self["textsrc"] = _v
        _v = arg.pop("uid", None)
        _v = uid if uid is not None else _v
        if _v is not None:
            self["uid"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("vertexcolor", None)
        _v = vertexcolor if vertexcolor is not None else _v
        if _v is not None:
            self["vertexcolor"] = _v
        _v = arg.pop("vertexcolorsrc", None)
        _v = vertexcolorsrc if vertexcolorsrc is not None else _v
        if _v is not None:
            self["vertexcolorsrc"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        _v = arg.pop("x", None)
        _v = x if x is not None else _v
        if _v is not None:
            self["x"] = _v
        _v = arg.pop("xcalendar", None)
        _v = xcalendar if xcalendar is not None else _v
        if _v is not None:
            self["xcalendar"] = _v
        _v = arg.pop("xhoverformat", None)
        _v = xhoverformat if xhoverformat is not None else _v
        if _v is not None:
            self["xhoverformat"] = _v
        _v = arg.pop("xsrc", None)
        _v = xsrc if xsrc is not None else _v
        if _v is not None:
            self["xsrc"] = _v
        _v = arg.pop("y", None)
        _v = y if y is not None else _v
        if _v is not None:
            self["y"] = _v
        _v = arg.pop("ycalendar", None)
        _v = ycalendar if ycalendar is not None else _v
        if _v is not None:
            self["ycalendar"] = _v
        _v = arg.pop("yhoverformat", None)
        _v = yhoverformat if yhoverformat is not None else _v
        if _v is not None:
            self["yhoverformat"] = _v
        _v = arg.pop("ysrc", None)
        _v = ysrc if ysrc is not None else _v
        if _v is not None:
            self["ysrc"] = _v
        _v = arg.pop("z", None)
        _v = z if z is not None else _v
        if _v is not None:
            self["z"] = _v
        _v = arg.pop("zcalendar", None)
        _v = zcalendar if zcalendar is not None else _v
        if _v is not None:
            self["zcalendar"] = _v
        _v = arg.pop("zhoverformat", None)
        _v = zhoverformat if zhoverformat is not None else _v
        if _v is not None:
            self["zhoverformat"] = _v
        _v = arg.pop("zsrc", None)
        _v = zsrc if zsrc is not None else _v
        if _v is not None:
            self["zsrc"] = _v

        # Read-only literals
        # ------------------

        self._props["type"] = "mesh3d"
        arg.pop("type", None)

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
