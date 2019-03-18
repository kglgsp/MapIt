import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
/*
 * @Author : Arpit Mandliya
 * Numerous Modifications made by Nathan Mueller
 */
public class JSONRead {

    JSONParser parser;

    public JSONRead() {
        this.parser = new JSONParser();
    }

    public JSONArray createJSONArray(String filename) {

        try {

            Object obj = parser.parse(new FileReader(filename));

            JSONArray jsonArray = (JSONArray) obj;

            return jsonArray;

/*
            Iterator i = jsonArray.iterator();
            while (i.hasNext()) {
                JSONObject o = (JSONObject) i.next();
                System.out.println(o.get("created_at"));
            }
            */

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }
        return null;
    }
}