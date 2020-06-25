from QAParser import parse, qaoutput
from datetime import datetime

qas = parse("questions.txt")
# qaoutput(qas)
header = open("header.html", "r")
faqpage = open("index.html", "w")
faqpage.write(header.read())
header.close()


for cat, questions in qas.items():
    faqpage.write("<br><br>\n<h4>{0}:</h4>".format(cat))
    for question in questions:
        entry = """
<!-- {0} -->
<button class="collapsible">{1}</button>
<div class="content">
  <br><p>{2}</p>
</div>\n""".format(*question)
        faqpage.write(entry)

today = datetime.now().strftime("%m/%d/%Y")
faqpage.write(r"""
<br><br><br><br><br>
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

<nav class="modal-footer" style="background-color: #607d8b;" id = "bottomL">
  <div class="col" style="color:#FFFF; text-align:left">Made by Zachary Hunt at TAMU Howdy Hack 2019.</div>
  <div class="col" style="color:#FFFF; text-align:right">Last Updated: {0}</div>
</nav>
</div>
  </body>
</html>""".replace("{0}", today))   # Is the the correct way to do this? No, most definitely certainly it is not.
# Am I going to leave it? Yes. Why? I intend to update this with properly done HTML at some point, and .format()
# is behaving in a way I don't care to understand. Deal with it :)

faqpage.close()
