#!/usr/bin/env nextflow

process BashExample {
    output: 
    stdout bash_result
    """
    echo "Hello from bash..."
    """
}

process pythonExample {
    output:
    stdout python_result
    """
    #!/usr/bin/env python3
    print("Hello from python World!")
    """
}

process juliaExample {
    output:
    stdout julia_result
    """
    #!/usr/bin/env julia
    println("Julia says hello")
    """
}

process pythonScriptExample {
    output:
    stdout script_result
    """
    example.py
    """
}

bash_result.view()
python_result.view()
julia_result.view()
script_result.view()
