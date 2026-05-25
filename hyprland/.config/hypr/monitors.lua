------------------
---- MONITORS ----
------------------

hl.monitor({
    output = "desc:IWB PC Monitor",
    mode = "preferred",
    position = "auto",
    scale = 2,
    mirror = "eDP-1",
})

hl.monitor({
    output = "desc:JVC LT-MK24220",
    mode = "1920x1080@100.0",
    position = "1600x0",
    scale = 1,
    bitdepth = 10,
})

hl.monitor({
    output = "eDP-1",
    mode = "1920x1080@60.01",
    position = "0x180",
    scale = 1.2,
})

hl.monitor({
    output = "",
    mode = "preffered",
    position = "auto",
    scale = 1,
})
