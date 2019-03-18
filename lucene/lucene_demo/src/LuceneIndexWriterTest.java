import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.Term;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.TermQuery;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.search.ScoreDoc;

import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;

public class LuceneIndexWriterTest {

    static final String INDEX_PATH = "/Users/nathanaelmueller/IdeaProjects/lucene_demo/index/";
    static final String JSON_FILE_PATH = "/Users/nathanaelmueller/IdeaProjects/lucene_demo/tweets_array.json";


    //test
    public void testWriteIndex(){
        try {
            LuceneIndexWriter lw = new LuceneIndexWriter(INDEX_PATH, JSON_FILE_PATH);
            lw.createIndex();
            //Check the index has been created successfully
            Directory indexDirectory = FSDirectory.open(Paths.get(INDEX_PATH));
            IndexReader indexReader = DirectoryReader.open(indexDirectory);
            int numDocs = indexReader.numDocs();
            if (numDocs == 1) System.out.println("index success");
            for ( int i = 0; i < numDocs; i++)
            {
                Document document = indexReader.document( i);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public void testQueryLucene() throws IOException, ParseException {
        Directory indexDirectory = FSDirectory.open(Paths.get(INDEX_PATH));
        IndexReader indexReader = DirectoryReader.open(indexDirectory);
        final IndexSearcher indexSearcher = new IndexSearcher(indexReader);
        Term t = new Term("text", "Disney");
        Query query = new TermQuery(t);
        TopDocs topDocs = indexSearcher.search(query, 15);


    }

}