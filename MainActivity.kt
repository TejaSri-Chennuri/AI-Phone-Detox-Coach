import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.provider.Settings
import androidx.appcompat.app.AppCompatActivity
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import android.app.AppOpsManager
import android.content.Context
import android.content.pm.PackageManager
import android.util.Log // Import for logging

private const val REQUEST_USAGE_STATS_PERMISSION = 1000

class MainActivity : AppCompatActivity() {

    private lateinit var usageStatsTextView: TextView
    private lateinit var getUsageStatsButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Initialize UI elements using findViewById()
        usageStatsTextView = findViewById(R.id.usageStatsTextView) //  Make sure you have this TextView in your activity_main.xml
        getUsageStatsButton = findViewById(R.id.getUsageStatsButton) // and this Button

        // Set a click listener for the button
        getUsageStatsButton.setOnClickListener {
            // Check for usage stats permission when the button is clicked
            if (!hasUsageStatsPermission()) {
                // Request permission by opening the Usage Access settings
                requestUsageStatsPermission()
            } else {
                // Permission already granted, proceed to retrieve usage stats
                retrieveUsageStats()
            }
        }

        //check permission on Activity start.
        if(hasUsageStatsPermission()){
            retrieveUsageStats()
        }

    }

    // Function to check if the app has the Usage Stats permission
    private fun hasUsageStatsPermission(): Boolean {
        val appOps = getSystemService(Context.APP_OPS_SERVICE) as AppOpsManager
        val mode = appOps.checkOpNoThrow(
            AppOpsManager.OPSTR_GET_USAGE_STATS,
            android.os.Process.myUid(),
            packageName
        )
        return mode == AppOpsManager.MODE_ALLOWED
    }

    // Function to request the Usage Stats permission from the user
    private fun requestUsageStatsPermission() {
        try {
            // Create an intent to open the Usage Access settings page
            val intent = Intent(Settings.ACTION_USAGE_ACCESS_SETTINGS).apply {
                data = Uri.parse("package:$packageName") // Specify the app's package name
            }
            startActivityForResult(intent, REQUEST_USAGE_STATS_PERMISSION) // Start the activity for result
        } catch (e: Exception) {
            // Handle exceptions, such as the settings activity not being available
            Toast.makeText(this, "Cannot open Usage Access Settings", Toast.LENGTH_LONG).show()
            Log.e("MainActivity", "Error opening Usage Access Settings: ${e.message}") // Log the error
        }
    }

    // Function to handle the result of the permission request
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == REQUEST_USAGE_STATS_PERMISSION) {
            // Check if the permission was granted
            if (hasUsageStatsPermission()) {
                // Permission granted, now retrieve usage stats
                retrieveUsageStats()
            } else {
                // Permission denied, inform the user
                Toast.makeText(
                    this,
                    "Usage Stats permission is required to access app usage data.",
                    Toast.LENGTH_LONG
                ).show()
                usageStatsTextView.text = "Permission Denied" // Update the TextView
            }
        }
    }

    // Function to retrieve usage stats (this is where you'll add the core logic)
    private fun retrieveUsageStats() {
        usageStatsTextView.text = "Retrieving usage stats..." // Initial message

        Log.d("UsageStats", "retrieveUsageStats() called") // Use Log for debugging

        usageStatsTextView.text = "Permission Granted! Now implement the UsageStatsManager query."

        // IMPORTANT:  You'll need to add code here to:
        // 1. Get an instance of UsageStatsManager.
        // 2. Define the time range for the data you want to retrieve.
        // 3. Call queryUsageStats or queryUsageStatsForInterval to get the data.
        // 4. Process the data and display it in the usageStatsTextView.
        //    or log it.
    }
}



