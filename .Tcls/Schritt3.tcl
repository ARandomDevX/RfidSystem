#############################################################################
# Generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#  Jun 13, 2019 03:15:31 PM CEST  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#
    menu .pop45 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font {-family {Segoe UI} -size 9} \
        -foreground black -tearoff 1 
    vTcl:DefineAlias ".pop45" "Popupmenu1" vTcl:WidgetProc "" 1
    menu .pop46 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font {-family {Segoe UI} -size 9} \
        -foreground black -tearoff 1 
    vTcl:DefineAlias ".pop46" "Popupmenu2" vTcl:WidgetProc "" 1
    menu .pop47 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font {-family {Segoe UI} -size 9} \
        -foreground black -tearoff 1 
    vTcl:DefineAlias ".pop47" "Popupmenu3" vTcl:WidgetProc "" 1

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m48" -background {#d9d9d9} 
    wm focusmodel $top passive
    wm geometry $top 1440x837+485+226
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1444 881
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm iconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set site_3_0 $top.m48
    menu $site_3_0 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    ttk::style configure TSizegrip -background #d9d9d9
    vTcl::widgets::ttk::sizegrip::CreateCmd $top.tSi52 \
        -cursor size_nw_se 
    vTcl:DefineAlias "$top.tSi52" "TSizegrip1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TSizegrip -background #d9d9d9
    vTcl::widgets::ttk::sizegrip::CreateCmd $top.tSi53 \
        -cursor size_nw_se 
    vTcl:DefineAlias "$top.tSi53" "TSizegrip2" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TSizegrip -background #d9d9d9
    vTcl::widgets::ttk::sizegrip::CreateCmd $top.tSi54 \
        -cursor size_nw_se 
    vTcl:DefineAlias "$top.tSi54" "TSizegrip3" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TRadiobutton -background #d9d9d9
    ttk::style configure TRadiobutton -foreground #000000
    ttk::style configure TRadiobutton -font "TkDefaultFont"
    ttk::radiobutton $top.tRa55 \
        -variable {} -takefocus {} -text {Soll gerade angemeldet sein} 
    vTcl:DefineAlias "$top.tRa55" "TRadiobutton1" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $top.tEn56 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$top.tEn56" "TEntry1" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $top.tLa57 \
        -background {#d9d9d9} -foreground {#000000} -font TkDefaultFont \
        -relief flat -text Klasse 
    vTcl:DefineAlias "$top.tLa57" "TLabel1" vTcl:WidgetProc "Toplevel1" 1
    ttk::progressbar $top.tPr59 \
        -variable probar -value 1.0 
    vTcl:DefineAlias "$top.tPr59" "TProgressbar1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background #d9d9d9
    ttk::style configure TButton -foreground #000000
    ttk::style configure TButton -font "TkDefaultFont"
    ttk::button $top.tBu62 \
        -takefocus {} -text Fertig 
    vTcl:DefineAlias "$top.tBu62" "TButton1" vTcl:WidgetProc "Toplevel1" 1
    ttk::separator $top.tSe64
    vTcl:DefineAlias "$top.tSe64" "TSeparator1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tSi52 \
        -in $top -x 600 -relx 1 -y 440 -rely 1 -anchor se -bordermode inside 
    place $top.tSi53 \
        -in $top -x 0 -relx 1 -y 0 -rely 1 -anchor se -bordermode inside 
    place $top.tSi54 \
        -in $top -x 580 -relx 1 -y 430 -rely 1 -anchor se -bordermode inside 
    place $top.tRa55 \
        -in $top -x 70 -y 140 -anchor nw -bordermode ignore 
    place $top.tEn56 \
        -in $top -x 130 -y 100 -anchor nw -bordermode ignore 
    place $top.tLa57 \
        -in $top -x 70 -y 110 -anchor nw -bordermode ignore 
    place $top.tPr59 \
        -in $top -x 120 -y 260 -width 370 -relwidth 0 -height 22 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tBu62 \
        -in $top -x 260 -y 380 -anchor nw -bordermode ignore 
    place $top.tSe64 \
        -in $top -x 20 -y 300 -width 570 -anchor nw -bordermode inside 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
