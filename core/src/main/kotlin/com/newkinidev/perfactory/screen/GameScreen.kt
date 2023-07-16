package com.newkinidev.perfactory.screen

import com.badlogic.gdx.scenes.scene2d.ui.Image
import com.badlogic.gdx.Gdx
import com.badlogic.gdx.graphics.Texture
import com.badlogic.gdx.graphics.g2d.Batch
import com.badlogic.gdx.graphics.g2d.SpriteBatch
import com.badlogic.gdx.scenes.scene2d.Stage
import com.badlogic.gdx.utils.Scaling
import com.badlogic.gdx.utils.viewport.ExtendViewport
import com.newkinidev.perfactory.utils.GetResolution
import com.newkinidev.perfactory.utils.ResizeImg
import ktx.app.KtxScreen
import ktx.graphics.use
import ktx.log.logger
import java.awt.Dimension

class GameScreen : KtxScreen {
    private val stage : Stage = Stage(ExtendViewport(16f, 9f))
    private val player : Texture = ResizeImg(Texture("assets/player.png"), 32, 64)
    private val resolution : Dimension = GetResolution()

    override fun show() {
        log.debug { "GameScreen gets shown" }
        log.debug { "Resolution = ${resolution.width} * ${resolution.height}" }
        stage.addActor(
            Image(player).apply {
                setPosition(1f, 1f)
                setSize(1f,1f)
                setScaling(Scaling.fill)
            }
        )
    }

    override fun resize(width: Int, height: Int) {
        stage.viewport.update(width,height,true)
    }

    override fun render(delta: Float) {
        with(stage){
            act(delta)
            draw()
        }
    }
    
    override fun dispose() {
        log.debug { "end" }
        stage.dispose()
        player.dispose()
    }

    companion object{
        private val log = logger<GameScreen>()
    }
}
