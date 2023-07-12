package com.newkinidev.perfactory

import com.badlogic.gdx.Application
import com.badlogic.gdx.Gdx
import com.newkinidev.perfactory.screen.GameScreen
import ktx.app.KtxGame
import ktx.app.KtxScreen

class perfactory : KtxGame<KtxScreen>(){
    override fun create() {
        Gdx.app.logLevel = Application.LOG_DEBUG
        addScreen(GameScreen())
        setScreen<GameScreen>()
    }
}
