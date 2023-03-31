public class Constants {
    public static final int CELL_SIZE = 32;

    public static final int CELLS_COUNT_X = 20;
    public static final int CELLS_COUNT_Y = 20;

    public static final int INITIAL_SPAWN_CHANCE = 1; //%

    public static final int FPS = 5;

    public static final int SCREEN_WIDTH = CELLS_COUNT_X * CELL_SIZE;
    public static final int SCREEN_HEIGHT = CELLS_COUNT_Y * CELL_SIZE;
    public static final String SCREEN_NAME = "Snake";
}

public enum Sprite {
    BODY("circle"), CHERRIES("cherries");

    private Texture texture;

    private Sprite(String texturename){
        try {
            this.texture = TextureLoader.getTexture("PNG", new FileInputStream(new File("res/"+texturename+".png")));
        } catch (IOEXception e) {
            e.printStackTrace();
        }
    }

    public Texture getTexture(){
        return this.texture;
    }
}