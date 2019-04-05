a = "37"
p1 = 0
p2 = 1

until a.size >= 10 || (a[(a.size - 10)..a.size].include?  "077201")
  a_p1 = a[p1].to_i
  a_p2 = a[p2].to_i
  next_a = a_p1 + a_p2
  a += next_a.to_s
  p1 = (p1 + a_p1 + 1) % a.size
  p2 = (p2 + a_p2 + 1) % a.size
end
puts(a.index("077201"))
