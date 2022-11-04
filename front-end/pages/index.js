import Navbar from "../components/Navbar";
import Flare1 from "../components/flares/Flare1";
import Flare2 from "../components/flares/Flare2";
import Main from "../components/Main";

export default function HomePage() {
  return (
    <section className="w-screen h-screen bg-bgPrimary">
      <Navbar />
      <Main />
      <Flare1 />
      <Flare2 />
    </section>
  );
}
