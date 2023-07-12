package com.newkinidev.perfactory.screen

import com.badlogic.gdx.graphics.Texture
import com.badlogic.gdx.graphics.g2d.Batch
import com.badlogic.gdx.graphics.g2d.SpriteBatch
import com.newkinidev.perfactory.utils.GetResolution
import com.newkinidev.perfactory.utils.ResizeResolution
import ktx.app.KtxScreen
import ktx.graphics.use
import ktx.log.logger
import java.awt.Dimension

class GameScreen : KtxScreen {
    private val spriteBatch : Batch = SpriteBatch()
    private val player : Texture = ResizeResolution(Texture("assets/player.png"))
    private val resolution : Dimension = GetResolution()

    override fun show() {
        log.debug { "GameScreen gets shown" }
        log.debug { "Resolution = ${resolution.width} * ${resolution.height}" }
    }

    override fun render(delta: Float) {
        spriteBatch.use {
            it.draw(player, 0f,0f)
        }
    }

    companion object{
        private val log = logger<GameScreen>()
    }
}
