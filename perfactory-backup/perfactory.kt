package com.newkinidev.perfactory

import ktx.app.KtxGame
import ktx.app.KtxScreen

class FirstScreen : KtxGame<KtxScreen>(){
    override fun create() {
        addScreen(GameScreen())
        setScreen<GameScreen>()
    }
}
