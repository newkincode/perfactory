package com.newkinidev.perfactory.utils

import com.badlogic.gdx.Gdx
import com.badlogic.gdx.graphics.Texture
import com.badlogic.gdx.graphics.g2d.SpriteBatch

fun ResizeImg(texture: Texture, desiredWidth: Int, desiredHeight: Int): Texture {
    val originalWidth = texture.width
    val originalHeight = texture.height

    val scaleX = desiredWidth.toFloat() / originalWidth
    val scaleY = desiredHeight.toFloat() / originalHeight

    val resizedTexture = texture
    val spriteBatch = SpriteBatch().apply {
        begin()
        draw(texture, 0f, 0f, desiredWidth.toFloat(), desiredHeight.toFloat(), 0, 0, originalWidth, originalHeight, false, false)
        end()
    }

    spriteBatch.dispose()

    return resizedTexture
}
