
public class Quat {
    String  hang;
    String model;
    Float gia;
    Integer congSuat;
    Integer soHienTai;
    Boolean dangQuay;
    public Quat(String hang, String model, Float gia, Integer congSuat){
        this.hang = hang;
        this.model = model;
        this.gia = gia;
        this.congSuat = congSuat;
        this.soHienTai = 0;
        this.dangQuay = false;
    }
    public void bat(){
        this.soHienTai = 1;
        System.out.println("Thuc hien chua nang bat");

    }
    public void tat(){
        this.soHienTai = 0;
        System.out.println("Tat quat");
    }
    public void chuyenSo(int so){
        this.soHienTai =so;
        System.out.println("Chuyen doi so:" + so);
    }
    public void chuyenQuay(){
        if (this.soHienTai == 0)
        {
//            this.dangQuay = false ;
            System.out.println("Chuyen qua trang thai dung yen");
        }else {
//            this.dangQuay = true;
            System.out.println("Chuyen qua trang thai quay");
        }
    }

    @Override
    public String toString() {
        return "Quat{" +
                "hang='" + hang + '\'' +
                ", model='" + model + '\'' +
                ", gia=" + gia +
                ", congSuat=" + congSuat +
                ", soHienTai=" + soHienTai +
                ", dangQuay=" + dangQuay +
                '}';
    }


    public static void main(String[] args) {
        Quat quat3 = new Quat("Sony,", "73dndz", 99999.f, 700);
        quat3.bat();
        quat3.chuyenSo(0);
        quat3.chuyenQuay();
        System.out.println(quat3);
    }
}