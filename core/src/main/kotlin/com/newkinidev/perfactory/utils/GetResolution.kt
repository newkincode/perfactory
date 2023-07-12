package com.newkinidev.perfactory.utils

import java.awt.Dimension
import java.awt.Toolkit

fun GetResolution(): Dimension {
    val screenSize: Dimension = Toolkit.getDefaultToolkit().getScreenSize()
    return screenSize
}
