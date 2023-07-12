package com.newkinidev.perfactory.utils

import com.badlogic.gdx.Gdx
import com.badlogic.gdx.graphics.Texture

private fun resizeImage(imageWidth: Int, imageHeight: Int, screenWidth: Int, screenHeight: Int): Pair<Int, Int> {
    val aspectRatio = imageWidth.toDouble() / imageHeight.toDouble()
    val screenWidthDouble = screenWidth.toDouble()
    val screenHeightDouble = screenHeight.toDouble()

    if (imageWidth <= screenWidth && imageHeight <= screenHeight) {
        return Pair(imageWidth, imageHeight) // 이미지가 화면보다 작거나 같으면 크기 변경 없이 원래 크기 반환
    } else if (imageWidth > screenWidth && imageHeight <= screenHeight) {
        val resizedWidth = screenWidth
        val resizedHeight = (screenWidthDouble / aspectRatio).toInt()
        return Pair(resizedWidth, resizedHeight) // 이미지의 가로 길이가 화면보다 크면 가로 길이를 화면에 맞추고 세로 길이를 비율에 맞게 조정하여 반환
    } else if (imageWidth <= screenWidth && imageHeight > screenHeight) {
        val resizedHeight = screenHeight
        val resizedWidth = (screenHeightDouble * aspectRatio).toInt()
        return Pair(resizedWidth, resizedHeight) // 이미지의 세로 길이가 화면보다 크면 세로 길이를 화면에 맞추고 가로 길이를 비율에 맞게 조정하여 반환
    } else {
        val ratioWidth = screenWidthDouble / imageWidth.toDouble()
        val ratioHeight = screenHeightDouble / imageHeight.toDouble()
        val scaleFactor = if (ratioWidth < ratioHeight) ratioWidth else ratioHeight
        val resizedWidth = (imageWidth * scaleFactor).toInt()
        val resizedHeight = (imageHeight * scaleFactor).toInt()
        return Pair(resizedWidth, resizedHeight) // 이미지의 가로, 세로 길이가 화면보다 크면 비율에 맞게 가로, 세로 길이를 조정하여 반환
    }
}

fun ResizeResolution(texture: Texture): Texture {
    val screenWidth = Gdx.graphics.width
    val screenHeight = Gdx.graphics.height

    val resizedDimensions = resizeImage(texture.width, texture.height, screenWidth, screenHeight)
    val resizedWidth = resizedDimensions.first
    val resizedHeight = resizedDimensions.second

    val resizedTexture = texture
    resizedTexture.setFilter(Texture.TextureFilter.Linear, Texture.TextureFilter.Linear)
    resizedTexture.setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge)
    resizedTexture.setWrap(Texture.TextureWrap.Repeat, Texture.TextureWrap.Repeat)
    resizedTexture.setWrap(Texture.TextureWrap.MirroredRepeat, Texture.TextureWrap.MirroredRepeat)
    resizedTexture.setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge)
    resizedTexture.setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge)
    resizedTexture.setWrap(Texture.TextureWrap.Repeat, Texture.TextureWrap.Repeat)
    resizedTexture.setWrap(Texture.TextureWrap.MirroredRepeat, Texture.TextureWrap.MirroredRepeat)
    resizedTexture.setWrap(Texture.TextureWrap.ClampToEdge, Texture.TextureWrap.ClampToEdge)

    return resizedTexture
}
