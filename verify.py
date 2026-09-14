import subprocess, sys, os

def run_demo():
    base = os.path.dirname(os.path.abspath(__file__))
    script = os.path.join(base, "scripts", "demo.py")
    result = subprocess.run([sys.executable, script], capture_output=True, text=True)
    if result.returncode != 0:
        print("Demo failed:", result.stderr)
        return False
    # Check for expected strings
    output = result.stdout
    required = ["Marketing Random Forest Accuracy", "HR Decision Tree Accuracy", "Ops SVM Accuracy", "Ops k-NN Accuracy"]
    for req in required:
        if req not in output:
            print(f"Missing expected output: {req}")
            print("Output:", output[:500])
            return False
    print("Demo output OK")
    return True

if __name__ == "__main__":
    if run_demo():
        print("Verification PASSED")
        sys.exit(0)
    else:
        print("Verification FAILED")
        sys.exit(1)