class Main{

    private static boolean isExistRequested = false;

    private static int x=-1, y=0, direction=1, length=3;

    private static void main(String[] args) {
        GUI.init();
        generate_new_obj();
        while(!isExistRequested){
            input();
            move();
            GUI.draw();
            GUI.update(have_to_decrease);
        }
    }

    private static void move() {
        have_to_decrease=true;

        switch(direction){
            case 0:
                y++; break;
            case 1:
                x++; break;
            case 2:
                y--; break;
            case 3:
                x--; break;
        }

        if(x < 0 || x >= CELLS_COUNT_X || y < 0 || y >= CELLS_COUNT_Y){
            System.exit(1);
        }

        int next_cell_state = GUI.getState(x,y);

        if(next_cell_state>0){
            System.exit(1);
        }else{
            if(next_cell_state < 0){
                length++;
                generate_new_obj();
                have_to_decrease=false;
            }
            GUI.setState(x,y,length);
        }
    }

    private static void generate_new_obj() {
        int point = new Random().nextInt(CELL_COUNT_X * CELL_COUNT_Y - length);

        for(int i=0; i<CELLS_COUNT_X; i++){
            for(int j=0; j<CELLS_COUNT_Y; j++){
                if(GUI.getState(i,j) <= 0) {
                    if (point == 0) {
                        GUI.setState(i, j, -1);
                        return;
                    } else {
                        point--;
                    }
                }
            }
        }
    }

    private static void input(){
        int newdirection = direction;

        while(Keyboard.next()){
            if(Keyboard.getEventKeyState()){
                switch(Keyboard.getEventKey()){

                    case Keyboard.KEY_ESCAPE:
                        isExistRequested = true;
                        break;
                    case Keyboard.KEY_UP:
                        if(direction!=2) newdirection=0;
                        break;
                    case Keyboard.KEY_RIGHT:
                        if(direction!=3) newdirection=1;
                        break;
                    case Keyboard.KEY_DOWN:
                        if(direction!=0) newdirection=2;
                        break;
                    case Keyboard.KEY_LEFT:
                        if(direction!=1) newdirection=3;
                        break;
                }
            }
        }
        direction = newdirection;

        isExistRequested = isExistRequested || Display.isCloseRequested();
    }
}