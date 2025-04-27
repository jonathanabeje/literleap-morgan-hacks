class StoryAnimator {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.svgNamespace = "http://www.w3.org/2000/svg";
        this.currentScene = null;
        this.scenes = [];
        this.currentSceneIndex = 0;
        this.isPlaying = false;
    }

    async loadSprites() {
        const response = await fetch('/static/images/story-sprites.svg');
        const svgText = await response.text();
        const parser = new DOMParser();
        const spritesDoc = parser.parseFromString(svgText, 'image/svg+xml');
        const defs = spritesDoc.querySelector('defs');
        this.container.appendChild(defs.cloneNode(true));
    }

    createScene(background = 'background-room') {
        const scene = document.createElementNS(this.svgNamespace, "g");
        scene.classList.add('scene');
        
        // Add background
        const bg = document.createElementNS(this.svgNamespace, "use");
        bg.setAttributeNS(null, "href", `#${background}`);
        scene.appendChild(bg);
        
        return scene;
    }

    addCharacter(scene, type = 'character-basic', x = 0, y = 0) {
        const character = document.createElementNS(this.svgNamespace, "use");
        character.setAttributeNS(null, "href", `#${type}`);
        character.setAttributeNS(null, "x", x);
        character.setAttributeNS(null, "y", y);
        character.classList.add('character');
        scene.appendChild(character);
        return character;
    }

    addProp(scene, type, x = 0, y = 0) {
        const prop = document.createElementNS(this.svgNamespace, "use");
        prop.setAttributeNS(null, "href", `#${type}`);
        prop.setAttributeNS(null, "x", x);
        prop.setAttributeNS(null, "y", y);
        scene.appendChild(prop);
        return prop;
    }

    addEffect(scene, type, x = 0, y = 0) {
        const effect = document.createElementNS(this.svgNamespace, "use");
        effect.setAttributeNS(null, "href", `#${type}`);
        effect.setAttributeNS(null, "x", x);
        effect.setAttributeNS(null, "y", y);
        scene.appendChild(effect);
        return effect;
    }

    async animateCharacter(character, animation, duration = 1000) {
        return new Promise(resolve => {
            character.classList.add(animation);
            setTimeout(() => {
                character.classList.remove(animation);
                resolve();
            }, duration);
        });
    }

    async moveCharacter(character, targetX, targetY, duration = 1000) {
        const startX = parseFloat(character.getAttributeNS(null, "x"));
        const startY = parseFloat(character.getAttributeNS(null, "y"));
        const startTime = performance.now();

        return new Promise(resolve => {
            const animate = (currentTime) => {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);

                const currentX = startX + (targetX - startX) * progress;
                const currentY = startY + (targetY - startY) * progress;

                character.setAttributeNS(null, "x", currentX);
                character.setAttributeNS(null, "y", currentY);

                if (progress < 1) {
                    requestAnimationFrame(animate);
                } else {
                    resolve();
                }
            };

            requestAnimationFrame(animate);
        });
    }

    addScene(sceneSetup) {
        const scene = this.createScene(sceneSetup.background);
        scene.style.opacity = 0;
        // Store last added character for animation targeting
        let lastCharacter = null;
        const wrappedActions = (sceneSetup.actions || []).map(action => {
            if (action.type === 'add_character') {
                // Mark this as the last character
                return { ...action, _isCharacter: true };
            }
            return action;
        });
        this.scenes.push({
            element: scene,
            actions: wrappedActions,
            lastCharacter: null
        });
        this.container.appendChild(scene);
        return scene;
    }

    async playScene(sceneIndex) {
        if (sceneIndex >= this.scenes.length) return;

        const scene = this.scenes[sceneIndex];
        const prevScene = this.scenes[sceneIndex - 1];

        // Fade out previous scene
        if (prevScene) {
            prevScene.element.style.transition = 'opacity 0.5s';
            prevScene.element.style.opacity = 0;
        }

        // Fade in current scene
        scene.element.style.transition = 'opacity 0.5s';
        scene.element.style.opacity = 1;
        this.currentScene = scene;

        // Execute scene actions
        for (const action of scene.actions) {
            await this.executeAction(action);
        }
    }

    async executeAction(action) {
        switch (action.type) {
            case 'add_character': {
                const character = this.addCharacter(
                    this.currentScene.element,
                    action.characterType,
                    action.x,
                    action.y
                );
                this.currentScene.lastCharacter = character;
                return character;
            }
            case 'addProp': {
                return this.addProp(
                    this.currentScene.element,
                    action.propType,
                    action.x,
                    action.y
                );
            }
            case 'move': {
                let target = action.target;
                if (!target && this.currentScene.lastCharacter) target = this.currentScene.lastCharacter;
                return this.moveCharacter(
                    target,
                    action.x,
                    action.y,
                    action.duration
                );
            }
            case 'animate': {
                let target = action.target;
                if (!target && this.currentScene.lastCharacter) target = this.currentScene.lastCharacter;
                return this.animateCharacter(
                    target,
                    action.animation,
                    action.duration
                );
            }
            case 'add_effect': {
                return this.addEffect(
                    this.currentScene.element,
                    action.effectType,
                    action.x,
                    action.y
                );
            }
            case 'delay': {
                return new Promise(resolve => setTimeout(resolve, action.duration));
            }
        }
    }

    async play() {
        if (this.isPlaying) return;
        this.isPlaying = true;
        
        for (let i = 0; i < this.scenes.length; i++) {
            if (!this.isPlaying) break;
            await this.playScene(i);
        }
        
        this.isPlaying = false;
    }

    pause() {
        this.isPlaying = false;
    }

    reset() {
        this.scenes.forEach(scene => {
            scene.element.style.opacity = 0;
        });
        this.currentSceneIndex = 0;
        this.isPlaying = false;
    }
}

// Example usage:
/*
const animator = new StoryAnimator('animation-container');
await animator.loadSprites();

const scene1 = animator.addScene({
    background: 'background-room',
    actions: [
        {
            type: 'add_character',
            characterType: 'character-happy',
            x: 100,
            y: 300
        },
        {
            type: 'move',
            target: character,
            x: 200,
            y: 300,
            duration: 2000
        },
        {
            type: 'animate',
            target: character,
            animation: 'jump',
            duration: 1000
        }
    ]
});

animator.play();
*/ 