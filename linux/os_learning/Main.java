import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Main {

    public static void main(String[] args) {
        // 스레드 풀을 생성하여 태스크를 비동기적으로 실행
        ExecutorService executor = Executors.newFixedThreadPool(3);

        // 파일 읽기 태스크 정의
        Callable<String> readFileTask = () -> {
            StringBuilder content = new StringBuilder();
            try (BufferedReader reader = new BufferedReader(new FileReader("sample.txt"))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    content.append(line).append("\n");
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
            return content.toString();
        };

        // 단어 세기 태스크 정의
        Callable<Integer> countWordsTask = () -> {
            String content = readFileTask.call();
            return content.split("\\s+").length;
        };

        try {
            // 파일 읽기 태스크 실행
            Future<String> fileContentFuture = executor.submit(readFileTask);
            String content = fileContentFuture.get();

            // 단어 세기 태스크 실행
            Future<Integer> wordCountFuture = executor.submit(countWordsTask);
            int wordCount = wordCountFuture.get();

            System.out.println("파일 내용:");
            System.out.println(content);
            System.out.println("단어 수: " + wordCount);

            // 외부 프로세스를 사용하여 결과 출력
            ProcessBuilder processBuilder = new ProcessBuilder();
            processBuilder.command("bash", "-c", "echo '단어 수: " + wordCount + "'");
            Process process = processBuilder.start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            int exitCode = process.waitFor();
            System.out.println("\n프로세스 종료, exit code: " + exitCode);

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            executor.shutdown();
        }
    }
}
