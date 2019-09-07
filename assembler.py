from QAParser import parse, qaoutput

qas = parse("questions.txt")
# qaoutput(qas)
header = open("header.html", "r")
faqpage = open("index.html", "w")
faqpage.write(header.read())
header.close()


for cat, questions in qas.items():
    faqpage.write("<br>\n<h4>{0}:</h4>".format(cat))
    for question in questions:
        entry = """
<!-- {0} -->
<button class="collapsible">{1}</button>
<div class="content">
  <br><p>{2}</p>
</div>\n""".format(*question)
        faqpage.write(entry)

faqpage.write("""
<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
</script>

<nav class="navbar fixed-bottom navbar-light bg-light ">
  <h6 class-"text-warning">Harshank and Zachary</h6>
</nav>
</div>
  </body>
</html>""")

faqpage.close()
