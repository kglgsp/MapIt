import java.io.IOException;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.document.*;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.index.IndexWriter;

import java.io.*;
import java.nio.file.Paths;
import java.util.List;
import java.util.Set;

public class LuceneIndexWriter {

    String indexPath;
    String jsonFilePath;
    IndexWriter indexWriter = null;
    JSONRead jsonr;

    public LuceneIndexWriter(String indexPath, String jsonFilePath) {
        this.indexPath = indexPath;
        this.jsonFilePath = jsonFilePath;
        this.jsonr = new JSONRead();
    }
    // "/Users/nathanaelmueller/IdeaProjects/lucene_demo/tweets.json"
    public void createIndex(){
        JSONArray jsonObjects = jsonr.createJSONArray(this.jsonFilePath);
        openIndex();
        addDocuments(jsonObjects);
        finish();
    }

    public boolean openIndex(){
        try {
            Directory dir = FSDirectory.open(Paths.get(indexPath));
            Analyzer analyzer = new StandardAnalyzer();
            IndexWriterConfig iwc = new IndexWriterConfig(analyzer);
            //Always overwrite the directory
            iwc.setOpenMode(IndexWriterConfig.OpenMode.CREATE);
            indexWriter = new IndexWriter(dir, iwc);
            return true;
        } catch (Exception e) {
            System.err.println("Error opening the index. " + e.getMessage());
        }
        return false;
    }

    public void addDocuments(JSONArray jsonObjects){
        for(JSONObject object : (List<JSONObject>) jsonObjects){
            Document doc = new Document();

            doc.add(new StringField("id", (String)object.get("id_str"), Field.Store.YES));

            doc.add(new StringField("text", (String)object.get("text"), Field.Store.YES));

            JSONObject user = (JSONObject) object.get("user");
            doc.add(new StringField("screen_name", (String)user.get("screen_name"), Field.Store.YES));

            /*
            JSONObject o_coordinates = (JSONObject) object.get("coordinates");
            JSONArray i_coordinates = (JSONArray) o_coordinates.get("coordinates");

            int counter = 0;
            for (Object o : i_coordinates) {
                System.out.println(o);
                if (counter == 0) {
                    DoublePoint field = new DoublePoint("x_coordinate", o, Field.Store.YES);
                    doc.add(field);
                }
                if (counter == 1) {
                    DoublePoint field = new DoublePoint("y_coordinate", o, Field.Store.YES);
                    doc.add(field);
                }
                counter++;
            }
            */


            /*
            for(String field : (Set<String>) object.keySet()){
                Class type = object.get(field).getClass();


                if (field == "created_at" || field == "id" || field == "text") {
                    doc.add(new StringField(field, (String)object.get(field), Field.Store.NO));
                }

                else if (field == "user") {
                    JSONObject job = object.getJSONObject(field);
                    for(String innerfield : (Set<String>) object[field].keySet()){
                        Class innertype = object.get(field).getClass();
                        if (innerfield == "screen_name") {
                            doc.add(new StringField(innerfield, (String)object[field].get(field), Field.Store.NO));
                        }
                    }
                }
                else if (field == "coordinates") {
                    JSONObject job = object.getJSONObject(field);
                    for(String innerfield : (Set<String>) object[field].keySet()){
                        Class innertype = object.get(field).getClass();
                        if (innerfield == "coordinates") {
                            System.out.println((String)object[field].get(field));
                            doc.add(new StringField(innerfield, (String)object.get(field), Field.Store.NO));
                        }
                    }
                }

                if(type.equals(String.class)){
                    doc.add(new StringField(field, (String)object.get(field), Field.Store.NO));
                }
                else if(type.equals(Long.class)){
                    doc.add(new LongRange(field, (long)object.get(field), Field.Store.YES));
                }
                else if(type.equals(Double.class)){
                    doc.add(new DoubleRange(field, (double)object.get(field), Field.Store.YES));
                }
                else if(type.equals(Boolean.class)){
                    doc.add(new StringField(field, object.get(field).toString(), Field.Store.YES));
                }

            }
            JSONObject user = (JSONObject) object.get("user");
            */

            try {
                indexWriter.addDocument(doc);
            } catch (IOException ex) {
                System.err.println("Error adding documents to the index. " +  ex.getMessage());
            }
        }
    }

    public void finish(){
        try {
            indexWriter.commit();
            indexWriter.close();
        } catch (IOException ex) {
            System.err.println("We had a problem closing the index: " + ex.getMessage());
        }
    }

}
