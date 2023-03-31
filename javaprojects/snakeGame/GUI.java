initializeOpenGL()

private static Cell[][] cells;

    public static void draw() {
        glClear(GL_COLOR_BUFFER_BIT);

        for(Cell[] line:cells){
            for(Cell cell:line){
                drawElement(cell);
            }
        }

        getState(x,y){
            return cells[x][y].getState();
        }

        setState(x,y,state){
            cells[x][y].setState(state);
        }
    }

private static void drawElement(Cell, elem){
        if(elem.getSprite() == null) return;

        elem.getSprite().getTexture().bind();

        glBegin(GL_QUADS);
        glTextCoord2f(0,0);
        glVertex2f(elem.getX(), elem.getY()+elem.getHeight());
        glTextCoord2f(1,0);
        glVertex2f(elem.getX()+elem.getWidth(), elem.getY()+elem.getHeight());
        glTextCoord2f(1,1);
        glVertex2f(elem.getX()+elem.getWidth(), elem.getY());
        glTextCoord2f(0,1);
        glVertex2f(elem.getX(), elem.getY());
        glEnd();
    }

public static void update(boolean have_to_decrease) {
        updateOpenGL();

        for (Cell[] line:cells){
            for (Cell cell:line){
                cell.update(have_to_decrease)
            }
        }
    }

private static void updateOpenGL(){
        Display.update();
        Display.sync(FPS);
        }

public static void init(){
        initializeOpenGL();

        cells = new Cell[CELLS_COUNT_X][CELLS_COUNT_Y];

        Random rnd = new Random();

        for(int i=0; i<CELLS_COUNT_X; i++){
            for(int j=0; j<CELLS_COUNT_Y; j++){
                cells[i][j]=new Cell(i*CELL_SIZE, j*CELL_SIZE, (rnd.nextInt(100) < INITIAL_SPAWN_CHANCE?-1:0);
            }
        }
    }